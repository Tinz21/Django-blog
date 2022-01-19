from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostView(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView2(APIView):
    def put(self, request, pk):
        serializer = PostSerializer(Post.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: None):
        serializer = Post.objects.get(pk=pk)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
