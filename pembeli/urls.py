from django.urls import path
from . import views

app_name = "pembeli"

urlpatterns = [
    path("", views.indexp, name="indexp"),
    path("pilih", views.pilih, name="pilih"),
    path("dashboard", views.dashboard, name="dashboard"),
    path(r'^postendpoint/$', views.dashboard)
]