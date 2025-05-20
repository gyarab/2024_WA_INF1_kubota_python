from django.urls import path
from . import views

app_name="AplikaceUkol"
urlpatterns = [
    path('', views.index, name='index'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('manufacturers/<int:pk>/', views.manufacturer_detail, name='manufacturer_detail'),
    path('car_review/<id>/', views.car_review, name='car_review')
]