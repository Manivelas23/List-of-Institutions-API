from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import institutionSerializer
from .models import institution
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#generic viewset


class institutionViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = institutionSerializer
    queryset = institution.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

