from django.urls import path
from app.views import input_data,get_data

urlpatterns = [
    path('',input_data),
    path('data_page',get_data)
]