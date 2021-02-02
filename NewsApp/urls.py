from django.urls import path
from .views import index, bbc, techcrunch

urlpatterns = [
    path('', index, name = "index"),
    path('bbc/', bbc, name = 'BBC'),
    path('techcrunch/', techcrunch, name = 'techcrunch')
    


]