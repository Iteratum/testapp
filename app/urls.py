from django.urls import path
from . import views
urlpatterns = [
    path('BlogHost/', views.BlogHost, name="BlogHost"),
]
