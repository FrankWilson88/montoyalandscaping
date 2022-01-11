from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/logout', include('django.contrib.auth.urls')),
]
