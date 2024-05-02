from django.urls import path,include
from . import views
urlpatterns = [
    path('add_album/' , views.add_albums , name='add_album'),
    path('edit/<int:id>' , views.edit_albums , name='edit_album'),
    path('delete/<int:id>' , views.delete_album , name='delete_album'),
]