from django.urls import path, include

urlpatterns = [
    path('', include('semiRestful_tv_shows.urls')),
]
