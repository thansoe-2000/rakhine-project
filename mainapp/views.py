from django.shortcuts import render
from . models import *
# Create your views here.

def dashboard(request):
     districts = District.objects.all()
     townships = Township.objects.all()
     wards = Ward.objects.all()
     villages = Village.objects.all()
     context = {
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'wards':wards
     }
     return render(request, 'backend/layouts/dashboard.html', context)

def category(request):
     categories = Category.objects.all()
     context = {
          'categories':categories
     }
     return render(request, 'backend/pages/category.html', context)

def district(request):
     districts = District.objects.all()
     context = {
          'districts':districts,
     }

     return render(request, 'backend/pages/district.html', context)

def township(request):
     villages = Village.objects.all()
     wards = Ward.objects.all()

     townships = Township.objects.all()
     context = {
          'townships':townships,
          'villages':villages,
          'wards':wards
     }
     return render(request, 'backend/pages/township_detail.html', context)

def village(request):
     villages = Village.objects.all()
     context = {
          'villages':villages
     }
     return render(request, 'backend/pages/village.html', context)

def ward(request):
     wards = Ward.objects.all()
     context = {
          'wards':wards
     }
     return render(request, 'backend/pages/ward.html', context)


def township_detail(request, pk=id):
     districts = District.objects.all()
     townships = Township.objects.all()
     wards = Ward.objects.all()
     villages = Village.objects.all()
     township_townships = Township.objects.filter(district_id=pk)
     township_villages = Village.objects.filter(township_id=pk)
     township_wards = Ward.objects.filter(township_id=pk)
     context = {
          'township_townships':township_townships,
          'township_villages':township_villages,
          'township_wards':township_wards,
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'wards':wards
     }
     return render(request, 'backend/pages/township_detail.html', context)


def district_detail(request, pk=id):
     districts = District.objects.all()
     townships = Township.objects.all()
     wards = Ward.objects.all()
     villages = Village.objects.all()
     district_townships = Township.objects.filter(district_id=pk)
     district_villages = Village.objects.filter(township__district__id=pk)
     district_wards = Ward.objects.filter(township__district__id=pk)
     context = {
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'wards':wards,
          'district_townships':district_townships,
          'district_villages':district_villages,
          'district_wards':district_wards
     }
     return render(request, 'backend/pages/district_detail.html', context)