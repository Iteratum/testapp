from django.urls import path
from . import views
urlpatterns = [
    path('https://r-blog-jeyl.vercel.app', views.BlogHost, name="BlogHost"),
]
