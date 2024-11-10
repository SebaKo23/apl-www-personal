from django.urls import path, include
from . import views

urlpatterns = [
    path('osoba/<int:pk>/', views.osoba_detail),
    path('osoba/update/<int:pk>/', views.osoba_update),
    path('osoba/delete/<int:pk>/', views.osoba_delete),
    path('osoba/', views.osoba_list),
    path('osoba/search/', views.osoba_search),
    path('stanowisko/<int:pk>/', views.stanowisko_detail),
    path('stanowisko/', views.stanowisko_list),
    path('stanowisko/<int:stanowisko_id>/members/', views.stanowisko_members),
]