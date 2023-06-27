from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Vallet
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import ValletSerializer


# Create your views here.
class ValletViewSet(
    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated]
    serializer_class = ValletSerializer

    def get_queryset(self):
        return Vallet.objects.filter(user=self.request.user)
