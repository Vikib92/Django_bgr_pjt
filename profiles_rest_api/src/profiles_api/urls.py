from django.urls import path
from . import views

urlpatterns = [
    path('helo-view', views.HelloAPIView.as_view())
]