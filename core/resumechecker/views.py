from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import JobDescription
from .serializer import JobDescriptionSerializer

class JobDescriptionAPI(APIView):
    def get(self,request):
        queryset=JobDescription.objects.all()
        serializer=JobDescriptionSerializer(queryset,many=True)
        return Response({
            'status':True,
            'data':serializer.data
        })