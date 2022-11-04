from django.urls import path
from . import views

urlpatterns = [
    path('get-song', views.GetSongViews.as_view(), name='get-song'),
    path('create-song', views.CreateSongViews.as_view(), name='create-song'),
    path('get-artiste', views.GetArtisteViews.as_view(), name='get-artiste'),
    path('update-song/<int:pk>/', views.UpdateSongViews.as_view(), name='get-song'),
    path('delete-song/<int:pk>/', views.DeleteSongViews.as_view(), name="delete-song")
]