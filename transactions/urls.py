from django.contrib import admin
from django.urls import path
from .views import ValletViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"vallet", ValletViewSet, basename="vallet")
urlpatterns = router.urls

urlpatterns += []
