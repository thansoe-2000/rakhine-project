from django.shortcuts import render
from . models import *
# Create your views here.

def dashboard(request):
     districts = District.objects.all()
     townships = Township.objects.all()
     wards = Ward.objects.all()
     villages = Village.objects.all()
     allhomes = WardHome.objects.all()
     
     context = {
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'wards':wards,
          'allhomes':allhomes
          
         
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
     wardhomes = WardHome.objects.all()
     townships = Township.objects.all()
     context = {
          'townships':townships,
          'villages':villages,
          'wards':wards,
          'wardhomes':wardhomes
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
     wardhomes = WardHome.objects.all()
     context = {
          'wards':wards,
          'wardhomes':wardhomes
     }
     return render(request, 'backend/pages/ward.html', context)







def district_detail(request, pk=id):
     districts = District.objects.all()
     townships = Township.objects.all()
     wards = Ward.objects.all()
     villages = Village.objects.all()
     wardhomes = WardHome.objects.all()
     district_townships = Township.objects.filter(district_id=pk)
     district_villages = Village.objects.filter(township__district__id=pk)
     district_wards = Ward.objects.filter(township__district__id=pk)
     district_homes = WardHome.objects.filter(ward__township__district__id=pk)
     context = {
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'wards':wards,
          'district_townships':district_townships,
          'district_villages':district_villages,
          'district_wards':district_wards,
          'wardhomes':wardhomes,
          'district_homes':district_homes
          
          

     }
     return render(request, 'backend/pages/district_detail.html', context)

def township_detail(request, pk=id):
     districts = District.objects.all()
     townships = Township.objects.all()
     wards = Ward.objects.all()
     villages = Village.objects.all()
     wardhomes = WardHome.objects.all()
     township_townships = Township.objects.filter(district_id=pk)
     township_villages = Village.objects.filter(township_id=pk)
     township_homes = WardHome.objects.filter(ward__township__id=pk)
     township_wards = Ward.objects.filter(township_id=pk)
     context = {
          'wardhomes':wardhomes,
          'township_townships':township_townships,
          'township_villages':township_villages,
          'township_wards':township_wards,
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'wards':wards,
          'township_homes':township_homes
          
     }
     return render(request, 'backend/pages/township_detail.html', context)


def ward_detail(request, pk=id):
     wards = Ward.objects.all()
     wardhomes = WardHome.objects.all()
     districts = District.objects.all()
     townships = Township.objects.all()
     ward_homes = WardHome.objects.filter(ward__id=pk)
     villages = Village.objects.all()
     context = {
          'wards':wards,
          'wardhomes':wardhomes,
          'districts':districts,
          'townships':townships,
          'villages':villages,
          'ward_homes':ward_homes
          

     }
     return render(request, 'backend/pages/ward_detail.html', context)


     
     
   