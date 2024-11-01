from django.urls import path, include
from . import views

urlpatterns = [
    path('osoba/<int:pk>/', views.osoba_detail),
    path('osoba/', views.osoba_list),
    path('osoba/search/', views.osoba_search),
    path('stanowisko/<int:pk>/', views.stanowisko_detail),
    path('stanowisko/', views.stanowisko_list),
]