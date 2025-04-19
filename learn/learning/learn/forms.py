from django import forms
from .models import *

class chaimenuform(forms.Form):
    chai_menu = forms.ModelChoiceField(queryset=chaimenu.objects.all(),label="select chai varity")
