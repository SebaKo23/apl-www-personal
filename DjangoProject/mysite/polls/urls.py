from django.urls import path, include
from . import views

urlpatterns = [
    path('osoba/<int:pk>/', views.OsobaDetail.as_view(), name='osoba-detail'),
    path('osoba/', views.OsobaList.as_view(), name='osoba-list'),
    path('osoba/search/', views.OsobaSearch.as_view(), name='osoba-search'),
    path('stanowisko/<int:pk>/', views.StanowiskoDetail.as_view(), name='stanowisko-detail'),
    path('stanowisko/', views.StanowiskoList.as_view(), name='stanowisko-list'),
]