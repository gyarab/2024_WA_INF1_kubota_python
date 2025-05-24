from django.urls import path
from . import views

app_name="leon_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name = 'projects'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('project/<int:pk>', views.project, name = 'project'),
]