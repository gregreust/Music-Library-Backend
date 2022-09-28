from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_songs),
    path('<int:pk>/', views.song_by_id)
]