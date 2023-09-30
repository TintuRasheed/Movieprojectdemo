from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import MovieForm

# Create your views here.
def demo(request):
    ob=Movie.objects.all()
    context={
        'movie_list':ob
    }
    return render(request,'Home.html',context)

def Parti_id(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'movie.html',{'movie': movie})

def Add_data(request):
    if request.method=='POST':
        Mname=request.POST.get('name',)
        Mdesc=request.POST.get('desc',)
        Myear=request.POST.get('year',)
        Mimg=request.FILES['mImg']
        add=Movie(Name=Mname,Desc=Mdesc,year=Myear,Img=Mimg)
        add.save()
        return redirect('/')
    return render(request,'Add_data.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"Edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)  
        movie.delete()  
        return redirect('/')
    return render(request,'Delete.html')