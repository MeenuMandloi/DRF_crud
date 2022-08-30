from rest_framework import serializers
from .models import Details
from django.db.models import fields

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('name', 'email', 'mobile', 'address')

# class DetailSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     email = serializers.EmailField(max_length=20)
#     mobile = serializers.IntegerField(allow_null=True)
#     address = serializers.CharField(max_length=50)
#
#     def create(self, validated_data):
#         return Details.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.mobile = validated_data.get('mobile', instance.mobile)
#         instance.address = validated_data.get('address', instance.address)
#         instance.save()
#         return instance
