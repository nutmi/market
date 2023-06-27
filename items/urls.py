from .views import GenericAPIView
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"generic", GenericAPIView)
urlpatterns = router.urls

urlpatterns += []
