from django.urls import path
from .views import MyModelListCreateAPIView, MyModelRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', MyModelListCreateAPIView.as_view(), name='mymodel-list-create'),
    path('<int:pk>/', MyModelRetrieveUpdateDestroyAPIView.as_view(), name='mymodel-detail'),
]
