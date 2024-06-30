from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.LoginView.as_view(), name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout')
]