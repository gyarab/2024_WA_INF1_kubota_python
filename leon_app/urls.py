from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name="leon_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name = 'projects'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('project/<int:pk>', views.project, name = 'project'),
    path('login/', views.login_view, name = 'login'),
    path('settings/', views.settings, name = 'settings'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]