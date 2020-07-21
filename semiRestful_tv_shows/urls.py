from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('shows', views.index, name="home"), 
    path('shows/new', views.create_show, name="create_show"),
    path('shows/create', views.adds_show),
    path('shows/<id>/update', views.update_show),
    
    path('shows/<id>', views.view_show),
    path('shows/<id>/edit', views.edit_show),
    path('shows/<id>/delete', views.delete, name="delete_show"),
    
    
    
]