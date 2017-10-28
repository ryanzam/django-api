# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from myApi.models import gallery
from myApi.serializers import gallerySerializer


class galleryViewSet(viewsets.ModelViewSet):
    queryset = gallery.objects.all()
    serializer_class = gallerySerializer

