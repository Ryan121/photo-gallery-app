from django import forms
from django.forms import NumberInput, TextInput, ModelForm
from django.forms import Textarea, Select
from .models import Photo, Category

class ImageUploadForm(ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                           required=False,
                                           widget=forms.Select(attrs={'class': "userform-control"}))

    class Meta:
        model = Photo

        fields = ['category', 'image', 'description']