from django.urls import path

from MyMusic.album.views import add_album, album_details, edit_album, delete_album

urlpatterns = [
    path('add/', add_album, name='add-album'),
    path('detail/<int:pk>', album_details, name='album-details'),
    path('edit/<int:pk>', edit_album, name='edit-album'),
    path('delete/<int:pk>', delete_album, name='delete-album'),
]
