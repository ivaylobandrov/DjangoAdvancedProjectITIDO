from django.urls import path
from portal import views

urlpatterns = [
    path("", views.render_csv, name='render_csv'),
    path("average", views.average_price_and_energy, name='average'),
]