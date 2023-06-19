from django.contrib import admin
from django.urls import path,include
from .views import HomePageView,SnackListView,SnackDetailView,SnackCreateView


urlpatterns = [
    path('',SnackListView.as_view(),name="home"),
    path('<int:pk>/',SnackDetailView.as_view(), name="snack_detail"),
    path('create/',SnackCreateView.as_view(), name="snack_create"),
]