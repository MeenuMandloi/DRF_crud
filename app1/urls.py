from django.urls import path
from app1 import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_detail, name='add_items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update_items'),
    path('delete/<int:pk>/', views.delete_items, name='delete_items'),
    path('detail/<int:pk>/', views.view_detail, name='view_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
