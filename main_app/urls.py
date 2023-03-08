from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name="games_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
]
