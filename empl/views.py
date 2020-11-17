from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import VehicleForm,DriverForm,DieselForm,MaintenanceForm

# Create your views here.

def index(request):
    drivers = Driver.objects.all()[:5]
    vehicles = Vehicle.objects.all()[:5]
    diesels = Diesel.objects.all()[:5]
    spares = SpareParts.objects.all()[:5]
    maintains = Maintenance.objects.all()[:5]

    # posts = "HELLO"
    # return HttpResponse("A tha vek e aw.")
    context ={'drivers':drivers,
                'vehicles':vehicles,
                'diesels':diesels,
                'spares':spares,
                'maintains':maintains}
    return render(request,'ed/index.html',context)



def vehicles(request):
    vehi = Vehicle.objects.all()
    if request.method == "POST":
        form = VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save()
            try:
                f.save()
                return redirect('/vehicles')
            except:
                pass
                return redirect('/vehicles')
        
    else:
        form = VehicleForm()
    return render(request,'ed/postform.html',{'form':form,'vehi':vehi})

def drivers(request):
    driv = Driver.objects.all()
    if request.method == "POST":
        form = DriverForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save()
            try:
                f.save()
                return redirect('/drivers')
            except:
                pass
                return redirect('/drivers')
        
    else:
        form = DriverForm()
    return render(request,'ed/driverform.html',{'form':form,'driv':driv})

def diesels(request):
    dee = Diesel.objects.all()
    if request.method == "POST":
        form = DieselForm(request.POST,request.FILES)
        if form.is_valid():
            # f = form.save(commit=False)
            f = form.save()

            try:
                f.save()
                return redirect('/diesels')
            except:
                pass
                return redirect('/diesels')
        
    else:
        form = DieselForm()
    return render(request,'ed/dieselform.html',{'form':form,'dee':dee})

def maintenance(request):
    maintains= Maintenance.objects.all()
    if request.method == "POST":
        form = MaintenanceForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save()
            try:
                f.save()
                return redirect('/maintenance')
            except:
                pass
                return redirect('/maintenance')
        
    else:
        form = MaintenanceForm()
    return render(request,'ed/maintainform.html',{'form':form,'maintains':maintains})