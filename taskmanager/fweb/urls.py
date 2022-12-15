from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexF, name='homeF'),
    path('aboutF', views.aboutF, name='aboutF'),
    path('create', views.create, name='create'),
]
