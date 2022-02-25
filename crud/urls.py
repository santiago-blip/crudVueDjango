from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import Home

router = routers.DefaultRouter()
router.register('',Home,basename="home")

urlpatterns = [
    path('',include(router.urls))
]