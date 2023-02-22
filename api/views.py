from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Family
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class FamilyList(generics.ListAPIView):
    
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['name_id','name','info','clan','country',
		'last_update','has_content','condicion']

    def get_queryset(self):
        queryset = Family.objects.all()
        name = self.request.query_params.get("name", None)
        print(name)
        if name == "Aaron":
            queryset = queryset.filter(name=name)
        else:
            raise ValidationError(detail="size must be either 'large' or 'small'")
        return queryset
