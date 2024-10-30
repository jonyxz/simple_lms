from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from core.models import Course
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    dataCourse = Course.objects.all()
    return HttpResponse("Hello, World!")

def testing(request):
    dataCourse = Course.objects.all()
    dataCourse = serializers.serialize('json', dataCourse)
    return JsonResponse(dataCourse, safe=False)

def addData(request):
    course = Course(
        name="Belajar Django",
        description="Belajar Django dari awal",
        price=100000,
        teacher=User.objects.get(username="admin")
    )
    course.save()
    return JsonResponse({"message": "Data berhasil ditambahkan"})

def editData(request):
    course = Course.objects.filter(name_icontain="Belajar Django").first()
    course.price = 150000
    course.save()
    return JsonResponse({"message": "Data berhasil diubah"})

def deleteData(request):
    course = Course.objects.filter(name_icontain="Belajar Django").first()
    course.delete()
    return JsonResponse({"message": "Data berhasil dihapus"})