from django import forms
from django.forms import fields
from .models import Health
 
class helthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ('staff_no', 'reported', 'degrees', 'condition', 'note', 'is_deleted', 'creator', )
