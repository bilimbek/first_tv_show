from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    return HttpResponse('please go to /http://localhost:8000/shows')

def shows(request):
    context = {
        'all_show' : Show.objects.all()
    }
    return render (request, 'tv_show_app/index.html', context)

def showinfor(request, num):
    showx = Show.objects.get(id = num)
    context = {
        'id' : showx.id,
        'title': showx.title,
        'network' : showx.network,
        'release' : showx.release,
        'description' : showx.description,
        'last_update': showx.updated_at,
        'all_show' : Show.objects.all()
    }
    return render(request, 'tv_show_app/showinfor.html', context)

def createshow(request):
    return render(request, 'tv_show_app/create.html')

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release = request.POST['release']
        desc = request.POST['desc']
        new = Show.objects.create(title=title, network = network, release = release, description = desc)
    return redirect('/shows/'+str(new.id))

def edit(request, num):
    showx = Show.objects.get(id = num)
    context = {
        'id' : showx.id,
        'title': showx.title,
        'network' : showx.network,
        'release' : showx.release,
        'desc' : showx.description,
        'last_update': showx.updated_at,
        'all_show' : Show.objects.all()
    }
    return render(request, 'tv_show_app/createnew.html', context)

def update(request):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release = request.POST['release']
        description = request.POST['description']
        idnumber = request.POST['id']
        showedit = Show.objects.get(id=idnumber)
        showedit.title = title
        showedit.network = network
        showedit.release = release
        showedit.desc = description
        showedit.save()
    return redirect('/shows/'+str(idnumber))

def delete(request, num):
    showdelete = Show.objects.get(id=num)
    showdelete.delete()
    return redirect('/shows')