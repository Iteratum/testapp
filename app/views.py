from .models import Blog
from .serializer import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET', 'POST'])
def BlogHost(request, formate=None):
    try:
        blog = Blog.objects.all()
        serialize = BlogSerializer(blog, many=True).data
        return Response(serialize)
    except Blog.DoesNotExist:
            return Response(status=404)