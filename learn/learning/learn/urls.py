# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("", views.learn, name='learn'),
   path('<int:id>' , views.learn_detail, name='learn_detail'),
   path('chai_stores/', views.chai_stores, name='chai_stores'),
]
