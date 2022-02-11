from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts.api.serializers import PostSerializer
from posts.models import Post
from posts.api.permissions import IsAdminOrReadOnly


class PostView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        """
        Show all posts

        This endpoint shows all posts
        """
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        """
        Create a new post

        This endpoint create a new post, which contains the following files in a json object
        For create a post, a user msut be loged in

        {
            'title':'Django Rest', 
            'slug':'DjangoR',
            'user':'Pepe',
            'content':'Django Rest Framework is a python tool for create rest apis',
            'created_at':'date is automatically',
            'category':'Frameworks',
            'published':'True'
        }
        user and category are foreign keys of the users and categories models   
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView2(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def put(self, request, pk):
        """
        Update a post

        This endpoint allows a logged in user to update one of their posts
        """
        serializer = PostSerializer(Post.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: None):
        """
        Delete a post

        This endpoint allows a logged in user to delete one of their posts
        """
        serializer = Post.objects.get(pk=pk)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
