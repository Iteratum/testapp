from django.urls import path
from . import views
urlpatterns = [
    path('', views.BlogHost, name="BlogHost"),
]
