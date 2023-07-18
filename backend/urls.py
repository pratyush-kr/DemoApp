from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from backend import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
]