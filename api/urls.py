from django.urls import path
from .views import my_model_list, my_model_detail

urlpatterns = [
    path('', my_model_list),
    path('<int:pk>/', my_model_detail),
]
