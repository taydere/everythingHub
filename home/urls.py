from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('business/', views.business),
    #path('compsci/', views.compsci),
    path('mathpalace/', views.mathpalace),
    path('arithmeticpalace/', views.arithmeticpalace),
    path('networkingmain/', views.networkingmain),
    path('networkingNotes/', views.networkingNotes),
    path('networkingProjects/', views.networkingProjects),
]
