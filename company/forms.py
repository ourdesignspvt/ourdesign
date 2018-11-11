from django.db import models
from .models import *
from django import forms


class index_form(forms.ModelForm):

    class Meta:
        model = query
        fields ='__all__'

class appoint_form(forms.ModelForm):

    class Meta:
        model = appoint
        fields ='__all__'
