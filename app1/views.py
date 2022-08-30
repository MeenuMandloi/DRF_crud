from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404, get_list_or_404
from app1.models import Details
from app1.serializers import DetailSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create/',
        'Update': '/update/pk/',
        'Delete': '/delete/pk/'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_detail(request):
    serializer = DetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    if request.query_params:
        serializer = Details.objects.filter(**request.query_param.dict())
    else:
        serializer = Details.objects.all()

    if serializer:
        data = DetailSerializer(serializer, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_detail(request, pk):
    if request.method == 'GET':
        details = Details.objects.filter(pk=pk)
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def update_items(request, pk):
    deta = Details.objects.get(pk=pk)
    data = DetailSerializer(instance=deta, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Details, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
