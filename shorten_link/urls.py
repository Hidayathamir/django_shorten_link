from django.urls import path

from .views import home, redirect_link

urlpatterns = [
    path("", home, name="shorten_link-home"),
    path(
        "<str:shortened_link>/",
        redirect_link,
        name="shorten_link-redirect_link",
    ),
]
