# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['GET', 'POST'])
def my_model_list(request):
    if request.method == 'GET':
        my_models = MyModel.objects.all()
        serializer = MyModelSerializer(my_models, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def my_model_detail(request, pk):
    try:
        my_model = MyModel.objects.get(pk=pk)
    except MyModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MyModelSerializer(my_model)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MyModelSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
