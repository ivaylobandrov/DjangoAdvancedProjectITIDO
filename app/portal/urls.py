from django.urls import path
from portal import views

urlpatterns = [
    path("", views.render_csv, name='render_csv'),
]