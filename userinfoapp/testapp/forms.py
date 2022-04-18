 
from django import forms
from django.forms import ModelForm
from testapp.models import UserInfo
from django.contrib.auth.models import User

class UserInfoForm(ModelForm):
    class Meta:
        model= UserInfo
        fields= ('name','address','mobileno','email','blood_group','Identity_card_number','driving_licence_no','bank_ac_no','creditcard_no','atmcard_no',)


class UserSingupForm(ModelForm):
    class Meta:
        model= User
        fields = ['username','password','email','first_name','last_name']


# widgets = {
#    'name':forms.TextInput(attrs={'class':'form-control'}),
#    'address':forms.TextInput(attrs={'class':'form-control'}),
#    'mobileno':forms.NumberInput(attrs={'class':'form-control'}),
#    'email':forms.EmailInput(attrs={'class':'form-control'}),
#    'blood_group':forms.TextInput(attrs={'class':'form-control'}),
#    'Identity_card_number':forms.NumberInput(attrs={'class':'form-control'}),
#    'driving_licence_no':forms.NumberInput(attrs={'class':'form-control'}),
#    'bank_ac_no':forms.NumberInput(attrs={'class':'form-control'}),
#    'creditcard_no':forms.NumberInput(attrs={'class':'form-control'}),
#    'atmcard_no':forms.NumberInput(attrs={'class':'form-control'}),
#   }
        