from django.shortcuts import render
from .models import (
    Sliderr,
    ImageOne,
    AboutUs,
    Mushroom,
    OurSerices,
    Backrgoundd
)

# Create your views here.

def index(request):
    slider =  Sliderr.objects.all()
    one_img =  ImageOne.objects.first()
    about_us =  AboutUs.objects.first()
    mushroom =  Mushroom.objects.all()
    our_services =  OurSerices.objects.all()
    background =  Backrgoundd.objects.first()


    context = {
        'slider' :  slider,
        'one_img' :  one_img,
        'about_us' :  about_us,
        'mushroom' : mushroom,
        'our_services' :  our_services,
        'background' :  background
 
    }
    return render(request,'index.html',context)

# def about(request):
#     return render(request,'about.html')


# def health_benefits(request):
#     return render(request,'health_benefit.html')
