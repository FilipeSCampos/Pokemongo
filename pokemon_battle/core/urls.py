from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('select_pokemon/', views.select_pokemon, name='select_pokemon'),
    path('battle/', views.battle, name='battle'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('start_battle/', views.start_battle, name='start_battle'),
    path('choose_team/', views.choose_team, name='choose_team'),
    path('battle/', views.battle, name='battle'),
]


if settings.DEBUG:  # Apenas adicione essas rotas se estiver no modo de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
