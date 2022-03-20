from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

# первый способ создания апиб базовый APIView
from api.serializers import Postserializer
from blog.models import Post


class PostsApiView(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = Postserializer(post, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = Postserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post_created': serializer.data})



class PostApiView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = Postserializer(post)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "error with pk, Put is not allowed"})

        instance = Post.objects.get(pk=pk)
        serializer = Postserializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post_upd': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "error with pk, Delete is not allowed"})

        instance = Post.objects.get(pk=pk)
        instance.delete()
        return Response({'post_delete': 'post was deleted -' + str(pk)})

# второй способ создания апи с помощью дженериков


class AllPostsApiList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostsApiUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer


class PostsApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer

#самый простой и непонятный способ
class PstViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer



