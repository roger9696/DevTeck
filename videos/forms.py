from django import forms
from . import models



class UploadNewVideo(forms.ModelForm):
    class Meta:
        model = models.Videos
        fields = ['title', 'description','video_file', 'poster']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['profile_picture', 'age', 'email', 'gender', 'number', 'bio']


