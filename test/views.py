from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  default
from test import common
from test.serializers import khataserializer


class khatabook(APIView):
    def get(self, request, format=None):
        a=default.objects.all()
        serializer=khataserializer(a,  many=True)
        print(type(serializer.data))
        if len(serializer.data) >0:
            return Response(common.success_Response(serializer.data))
#             JsonResponse(common.success_Response(serializer.data))
        else:
            return Response(common.failure_Response(serializer.data))  
        
        
    def post(self, request, format=None):
        
        serializer = khataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)