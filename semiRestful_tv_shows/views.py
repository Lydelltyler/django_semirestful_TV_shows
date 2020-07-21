from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Shows


###### SENDS TO MAIN TABLE ROUTE

def home(request):
    return redirect('/shows')

####### SHOWS MAIN SHOW TABLES

def index(request):
    print(request.GET)
    context = {
        'show_table': Shows.objects.all()
    }

    return render(request, "showTable.html", context)

####### TEMPLATE FOR ADDING SHOWS

def create_show(request):
    print(request.GET)
    return render(request, "addShow.html")

####### TEMPLATE FOR EDITING SHOWS

def edit_show(request, id):
    
    this_id= int(id)
    
    context ={
        'show_info': Shows.objects.get(id=this_id)
    }

    print(request.GET)
    return render(request, "editShow.html", context)

######## ADDS SHOW TO DATABASE

def adds_show(request):
    
    errors = Shows.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/shows/new')
    else:
        title_from_form = request.POST['title']
        network_from_form = request.POST['network']
        release_from_form = request.POST['release_date']
        desc_from_form = request.POST['desc']
        Shows.objects.create(title=title_from_form, network=network_from_form,
                            release=release_from_form, desc=desc_from_form)
        lastest_id = Shows.objects.last()
        id = lastest_id.id
        print(id)
        return redirect(f'/shows/{id}')

####### UPDATES SHOW IN DATABASE

def update_show(request, id):
    this_id = int(id)
    
    errors = Shows.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect(f'/shows/{id}/edit')
    else:
        this_show = Shows.objects.get(id=this_id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release = request.POST['release_date']
        this_show.desc = request.POST['desc']
        this_show.save()
        messages.success(request, f"Show {id} successfully updated")
    
    print(this_id)
    print(request.POST)
    return redirect(f'/shows/{id}')


####### DISPLAY SHOW INFORMATION

def view_show(request, id):

    this_id = int(id)
    context = {
        'show_info': Shows.objects.get(id=this_id)
    }
    print(this_id)
    return render(request, 'showInfo.html', context)


######## TABLE ACTIONS

def show_methods(request):
    all_shows = Shows.objects.all()
    
    for key, value in request.POST.items():
        # FOR DELETED SHOWS
        if key == "delete_show":
            for show in all_shows:
                if show.id == int(request.POST['delete_show']):
                    print(show.id)
                    show.delete()
        # FOR EDITING SHOWS
        if key == "edit_show":
            for show in all_shows:
                if show.id == int(request.POST['edit_show']):
                    print(show.id)
                    return redirect(f'/shows/{show.id}/edit')
        # FOR VIEWING SHOWS
        if key == "view_show":
            for show in all_shows:
                if show.id == int(request.POST['view_show']):
                    # print(show.id)
                    return redirect(f'/shows/{show.id}' )
        
        print(key, value)
    print(request.POST)
    return redirect('/shows')
