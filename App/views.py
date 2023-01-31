from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    pics=Drones.objects.all()
    picture=Interactions.objects.all()
    pic=Services.objects.all()
    return render(request,'index.html',{'pc':pics, 'pt':picture, 'pi':pic})

