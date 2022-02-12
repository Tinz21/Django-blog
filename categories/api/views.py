from importlib.resources import path
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryView(ViewSet):

    permission_classes = [IsAdminOrReadOnly]
    def list(self, request):
        """
        Show all categories

        This method shows all categories
        """
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        """
        Create new category

        This method create a new category

        ---
        The category has the next fields :
        - title
        - slug
        - published: this field can be true or false
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk: None):
        """
        Update a category

        This method updates a category when its id is inserted in the url
        Example : http://0.0.0.0:8000/api/categories/{id}/
        """
        object_update = Category.objects.get(pk=pk)
        serializer = CategorySerializer(object_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk: None):
        """
        Remove a category

        This method removes a category using its id.
        """
        serializer = Category.objects.get(pk=pk)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
