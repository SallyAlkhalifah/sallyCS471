from django import forms
from django.db import models
from .models import Book
from .models import Book, Publisher, Author



class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'price', 'rating', 'author'] 
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget= forms.TextInput( attrs= {'placeholder':'','class':"mycssclass",'id':'jsID'}))
    
    price = forms.DecimalField(required=True,
        label="Price",
        initial=0)
    
    rating = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput())
    
    author = forms.ModelChoiceField(
        empty_label = None,
        queryset = Author.objects.all(),
        required=True,
        label="Author",
        widget= forms.Select( attrs= {
            'class':"mycssclass",'id':'jsID2'}))