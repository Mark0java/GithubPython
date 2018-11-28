from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_form),
    path('search/', views.search),
    path('buy/', views.buy),
    path('book/', views.book),
    path('profile/', views.profile),
    path('dismiss/', views.dismiss),
    path('buy_booked/', views.buy_booked),
    path('buy_booked/profile/', views.profile),
    path('dismiss/profile/', views.profile),
]