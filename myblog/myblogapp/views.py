from django.shortcuts import render
from .models import BLOG
from .serializers import BLOGSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def  get_all_blogs(request):
    blogs=BLOG.objects.all()
    serializer=BLOGSerializers(blogs,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_by_id(request,pk):
    try:
        blog=BLOG.objects.get(pk=pk)
    except BLOG.DoesNotExist:
        return Response(status=status.HTTP_40V_NOT_FOUND)
    serializer=BLOGSerializers(blog)
    return Response(serializer.data)


@api_view(['POST'])
def post_blog(request):
    serializer=BLOGSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_blog(request,pk):
    try:
        blog=BLOG.objects.get(pk=pk)
    except BLOG.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=BLOGSerializers(blog,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
