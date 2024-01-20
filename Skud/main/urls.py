from django.urls import include, path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("take_cards/", takeCard, name="take_cards"),
    path("return_cards/", returnCards, name="return_cards"),
    path("about/", about, name="about"),
    path("info/<slug:slug>/", info, name="info"),
]
