from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Classroom
from .serializers import StudentSerializer, ClassroomSerializer


# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context)


# ViewSets define the view behavior.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer