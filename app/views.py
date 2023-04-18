from django.shortcuts import render,redirect
from .models import OPSEmp
from django.contrib import messages
# Create your views here.

def index(request):
    data=OPSEmp.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    if request.method=="POST":
        badge_id=request.POST.get('badge_id')
        department=request.POST.get('department')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(badge_id,department,age,gender)
        query=OPSEmp(badge_id=badge_id,department=department,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        badge_id=request.POST['badge_id']
        department=request.POST['department']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=OPSEmp.objects.get(id=id)
        edit.badge_id=badge_id
        edit.department=department
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=OPSEmp.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=OPSEmp.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
    
    

def dashboard(request):
    return render(request,"dashboard.html")


def about(request):
    return render(request,"about.html")