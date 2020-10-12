from django import forms
from .models import Register
from django.forms import TextInput


class RegisterForm(forms.ModelForm):

    ID_CHOICES =( 
        ("1", "PAN"), 
        ("2", "Aadhar"), 
        ("3", "VoterID"), 
        ("4", "Others"), 
    ) 
    
    id_type = forms.ChoiceField(choices=ID_CHOICES,widget=forms.Select(attrs={"name": "select_0","class": "form-control"}))
    class Meta:
        model = Register
        fields = ['name','idcard_no','id_type','address','phone_no','email','meet_with']
        
        widgets ={'name': TextInput(attrs={'type':'text','class':"form-control", 'placeholder':"Enter your Name", 'name':"name"}),
                  'idcard_no': TextInput(attrs={'type':'text','class':"form-control", 'placeholder':"Enter your IDcard No", 'name':"idcard_no"}),
                  'address': TextInput(attrs={'type':'text','class':"form-control",'placeholder':"Enter your Address", 'name':"address" }),
                  'phone_no':TextInput(attrs={'type':'phone','class':"form-control",'placeholder':"Enter your Phone No", 'name':"phone_no"}),
                  'email':TextInput(attrs={'type':'email','class':"form-control",'placeholder':"Enter your Email", 'name':"email"}),
                  'meet_with':TextInput(attrs={'type':'text','class':"form-control",'placeholder':"With whom you wanna meet ?", 'name':"meet_with" }),
        } 


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        idcard_no = cleaned_data.get('idcard_no')
        id_type = cleaned_data.get('id_type') 
        address = cleaned_data.get('address')
        phone_no = cleaned_data.get('phone_no')
        email = cleaned_data.get('email')
        meet_with = cleaned_data.get('meet_with')   



