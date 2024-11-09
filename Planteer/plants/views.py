from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant
# Create your views here.

def home_view(request:HttpRequest):

    plant=Plant.objects.all()
    
    return render(request,"main/index.html",{"plant":plant})




def all_plants_view(request:HttpRequest):

    plant=Plant.objects.all()
    
    return render(request,"main/all_plants.html",{"plant":plant})


def add_plant(request:HttpRequest):
 if request.method == "POST":
        print("Is Edible:", request.POST.get("is_edible"))  # لتتبع القيمة
        
        new_plant = Plant(
            name=request.POST["name"],
            about=request.POST["about"],
            used_for=request.POST["used_for"],
            image=request.FILES.get("image"),
            category=request.POST.get("category"),
            is_edible=True if request.POST.get("is_edible") else False 
             )
    
        new_plant.save()
        return redirect('plants:home_view')
 return render(request,"main/add.html")







def post_detail(request:HttpRequest, plant_id:int):

    plant= Plant.objects.get(pk=plant_id)
    similarPlants = Plant.objects.filter(category=plant.category)[0:3]
    response = render(request, 'main/detial.html', context={"plant":plant, "similarPlants": similarPlants})

    

    return response



def post_update(request:HttpRequest,plant_id:int):

     plant= Plant.objects.get(pk=plant_id)
     if request.method == "POST":
         plant.name = request.POST["name"]
         plant.about = request.POST["about"]
        
       
         if "image" in request.FILES: plant.image = request.FILES["image"]
         plant.save()
       

         return redirect("plants:post_detail", plant_id=plant.id)
     
     return render(request, "main/post_update.html", {"plant" : plant})


   

def post_delete(request:HttpRequest,plant_id):

     plant= Plant.objects.get(pk=plant_id)
     plant.delete()
     return redirect('plants:home_view')



def search_view(request:HttpRequest):

    if "search" in request.GET:

        plant=Plant.objects.filter(name__contains=request.GET["search"])
    else:
        plant=[]

    return render(request,"main/search_plant.html",{"plant":plant})