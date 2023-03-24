from django.urls import path
from .views import home

APP_NAME = "game"

urlpatterns = [
    path("", home, name="game_home"),
]
