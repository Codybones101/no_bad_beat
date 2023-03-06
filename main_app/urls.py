from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bets/', views.bets_index, name="bets_index"),
    path('accounts/signup/', views.signup, name='signup'),
]
