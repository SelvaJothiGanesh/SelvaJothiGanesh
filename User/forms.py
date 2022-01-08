from django import forms
from User.models import User_Profile

# Create your models here.

class User_Form(forms.ModelForm):
    class Meta:
        model = User_Profile#.objects.filter(id=User_Profile.Id,name=User_Profile.Name)
        # fields = ('Id','Name')
        fields='__all__'
