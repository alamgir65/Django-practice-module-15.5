from django import forms 
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        
        labels = [
            ('album_name', 'Album Name'),
            ('release_date', 'Release Date'),
            ('ratings', 'Ratings'),
        ]
        