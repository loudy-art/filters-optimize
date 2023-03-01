from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Family
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
import urllib

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class FamilyList(generics.ListAPIView):

    def get_queryset(self):
        queryset = Family.objects.all()
        name = self.request.query_params.get('name')
       # finalname = urllib.parse.urlencode(name)
        exactMatch = self.request.query_params.get("exactMatch", None)
        history = self.request.query_params.get("history", None)
        crest = self.request.query_params.get("crest", None)
        prdImages = self.request.query_params.get("prdImages", None)
        itemsPerPage = self.request.query_params.get("itemsPerPage", None)
        page = self.request.query_params.get("page", None)
        history = self.request.query_params.get('history')

        #history
        if history == "true":
            self.serializer_class = FamilySerializerHistory  
            queryset = queryset.filter(name__contains=name)

        #crests
        elif crest == "true":
            self.serializer_class = FamilySerializerCrest
            queryset = queryset.filter(name=name)

        #products
        elif prdImages == "true":
            self.serializer_class = FamilySerializerProducts
            queryset = queryset.filter(name=name)

        #historyandcrests
        elif crest == "true" and history == "true":
            self.serializer_class = FamilySerializerHistoryCrest
            queryset = queryset.filter(name=name)

        #crestandproducts
        elif crest == "true" and prdImages == "true":
            self.serializer_class = FamilySerializerProductsCrest
            queryset = queryset.filter(name=name)

        #historyandproducts
        elif history == "true" and prdImages == "true":
            self.serializer_class = FamilySerializerHistoryProd
            queryset = queryset.filter(name=name)

        #empty
        else:
            self.serializer_class = FamilySerializerGeneral
            queryset = queryset.filter(name=name)


        return queryset
