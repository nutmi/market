from django.urls import path
from rest_framework import routers
from .views import ReviewViewSet

router = routers.DefaultRouter()
router.register(r"reviews", ReviewViewSet, basename="products")
urlpatterns = router.urls

urlpatterns += []