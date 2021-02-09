from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm


login_as=(
("Customer","Customer"),
("Retailer","Retailer"),
("Wholesaler","Wholesaler")

)
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    login_field=forms.ChoiceField(choices=login_as)


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","login_field")

class UpdateUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email address'}

class ProductForm(ModelForm):
    class Meta:
        model=Product
        exclude=['user',]

    


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2'] 
           
class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

        widgets ={
            'name': forms.TextInput(attrs={'placeholder':'Enter full name'}),
            'email': forms.TextInput(attrs={'placeholder':'Enter email'}),
            'address': forms.TextInput(attrs={'placeholder':'Enter address'}),
            'city': forms.TextInput(attrs={'placeholder':'Enter city'}),
            'state': forms.TextInput(attrs={'placeholder':'Enter state'}),
            'postcode': forms.TextInput(attrs={'placeholder':'Enter postcode'}),
            'phone': forms.TextInput(attrs={'placeholder':'Enter phone'}),
        }