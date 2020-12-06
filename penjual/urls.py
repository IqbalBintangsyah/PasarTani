from django.urls import path
from . import views

app_name = "penjual"

urlpatterns = [
    path("", views.index, name="index"),
    path("pub", views.pub_data, name="pub"),
    path("sub", views.sub_data, name="sub")
]