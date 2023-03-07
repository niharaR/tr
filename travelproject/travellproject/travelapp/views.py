from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
# from .models import Picture

# Create your views here.
# def demo(request):
#     return render(request,'index.html')
def demo(request):
    ob=Place.objects.all()
    return render(request,"index.html",{'result':ob})



# def demot(request):
#     obj=Picture.objects.all()
#     return render(request,"index.html",{'res':obj})