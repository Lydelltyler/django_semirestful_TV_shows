from django.shortcuts import render, HttpResponse, redirect
from .models import Shows


def index(request):
    print(request.GET)
    return render(request, "showTable.html")

def new_show(request):
    print(request.GET)
    return render(request, "addShow.html")

def add(request):
    title_from_form = request.POST['title']
    network_from_form = request.POST['network']
    release_from_form = request.POST['release_date']
    desc_from_form = request.POST['desc']
    Shows.objects.create(title=title_from_form, network=network_from_form,
                         release=release_from_form, desc=desc_from_form)
    lastest_id = Shows.objects.last()
    id = lastest_id.id
    print(id)
    return redirect(f'/shows/{id}', id=id)


def pages(request, id):

    context = {
        'show_info': Shows.objects.last()
    }

    return render(request, 'showInfo.html', context)

def delete_page(request):
    all_shows = Shows.objects.all()
    for show in all_shows:
        if show.id == int(request.POST['which_show']):
            print(show.id)
            show.delete()
        
    print(request.POST)
    return redirect('/')
