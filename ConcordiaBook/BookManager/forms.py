from django import forms
from .models import Textbooks

class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbooks
        fields = ['title', 'author', 'edition', 'condition', 'course_code']
        widgets = {'condition': forms.Select(choices=[('new', 'New'),('used', 'Used'),('old', 'Old'),("damaged", "Damaged")])}
