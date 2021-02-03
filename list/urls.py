from django.urls import path
from .import views

urlpatterns=[
    path('tally', views.tally),
    path('tally/create', views.create_tally),
    path('tally/delete/<int:tally_id>/', views.delete_tally),
]