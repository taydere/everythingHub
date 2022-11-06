from django.urls import path
from . import views
from .views import arithmeticPalaceView

urlpatterns = [
    path('', views.index),
    #path('business/', views.business),
    #path('compsci/', views.compsci),
    path('mathpalace/', views.mathpalace),
    path('arithmeticpalace/', arithmeticPalaceView.as_view(), name = "arith"),
    #path('arithmeticpalace/', views.arithmeticpalace),
    path('networkingmain/', views.networkingmain),
    path('networkingNotes/', views.networkingNotes),
    path('networkingProjects/', views.networkingProjects),
    path('programmingpalace/', views.programmingPalace),
    path('programmingFundamentals/', views.programmingFundamentals),
]
