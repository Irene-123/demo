from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Site 
from .serializers import SiteSerialilzer, switchSerializer, orderSerializer, IAPSerializer 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

def index(request):
    return HttpResponse("My first view")

class site_list(APIView):
    def get(self, request, format=None):
        sites= Site.objects.all() 
        serializer= SiteSerialilzer(sites, many=True) 
        return Response(serializer.data)
    def post(self, request, format=None):
        sites= request.data
        serializer= SiteSerialilzer(data= sites) 
        if serializer.is_valid():
            serializer.save() 
            return Response("Sites successfully added")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        pk= request.query_params.get('site_id', None) 
        if pk: 
            site= Site.objects.get(pk= pk) 
            serializer= SiteSerialilzer(instance=site, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('sites Updated')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pk = request.query_params.get('site_id', None)
        site = Site.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def site_list(request):
#     if request.method=='GET':
#         sites= Site.objects.all() 
#         serializer= SiteSerialilzer(sites, many=True) 
#         return Response(serializer.data)

#     elif request.method=='POST':
#         sites= request.data
#         serializer= SiteSerialilzer(data= sites) 
#         if serializer.is_valid():
#             serializer.save() 
#         return Response("Sites successfully added") 
#     elif request.method=='PUT':
#         pk= request.query_params.get('site_id', None) 
#         if pk: 
#             site= Site.objects.get(pk= pk) 
#             serializer= SiteSerialilzer(instance=site, data= request.data)
#             if serializer.is_valid():
#                 serializer.save()
#         return Response('sites Updated')
#     elif request.method == 'DELETE':
#         pk = request.query_params.get('site_id', None)
#         site = Site.objects.get(pk=pk).delete()
#         return Response('sites Deleted')

    




