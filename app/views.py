from .models import Blog
from .serializer import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def BlogHost(request, format=None):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serialize = BlogSerializer(blog, many=True)
        return Response(serialize.data)