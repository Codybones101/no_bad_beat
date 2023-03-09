from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name="games_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/<int:game_id>/add_bet/', views.add_bet, name='add_bet'),
    path('games/<int:game_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]

urlpatterns += staticfiles_urlpatterns()