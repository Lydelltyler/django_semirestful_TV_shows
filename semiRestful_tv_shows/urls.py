from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.new_show),
    path('shows/create', views.add),
    path('shows/<id>', views.pages),
    path('delete', views.delete_page)
]