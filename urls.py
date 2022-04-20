from .views import *
from django.urls import path,include
from rest_framework import routers
from knox import views as knox_views

#router = routers.DefaultRouter()
#router.register('api',UserProfileViewSet)

urlpatterns = [
path('api/register/', RegisterUserWithOutSession.as_view(), name='register'),
path('api/register/<str:ref_code>', RegisterUserAPIView.as_view(), name='register'),]
