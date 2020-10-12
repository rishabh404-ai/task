from django import forms
from .models import Register, Entry
from django.forms import TextInput
from .utils import Util
from django.core.mail import EmailMessage,send_mail

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
        
        widgets ={
            'name': TextInput(attrs={'type':'text','class':"form-control", 'placeholder':"Enter your Name", 'name':"name"}),
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

        # Error-Handling Validations 
        if not name:
            return forms.ValidationError('Failed : Name is Required ')

        if not idcard_no:
            return forms.ValidationError('Failed : Idcard No is Required ')   

        if not id_type:
            return forms.ValidationError('Failed : Id_Type is Required ')

        if not address:
            return forms.ValidationError('Failed : Address is Required ')

        if not phone_no:
            return forms.ValidationError('Failed : Phone No is Required ')

        if not email:
            return forms.ValidationError('Failed : Email is Required ')
        
        if not meet_with:
            return forms.ValidationError('Failed : You must specify the person you wanna meet')    

        # Email Config For New User     
        if email:
            email_body = 'Hello New User, Welcome to our office'
            data = {'email_body': email_body, 'to_email': email, 'email_subject': 'Thank You'}    
            Util.send_mail(data)
  
        # Email Config For Existing User  
        if Register.objects.filter(email=email).exists():

            user_email = Register.objects.get(email=email)
            email_body = 'Hello User,Welcome Back'
            data = {'email_body': email_body, 'to_email': user_email.email, 'email_subject': 'Thank You'}    
            Util.send_mail(data)

                        
class RecordEntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['person','start_time','end_time']
        widgets = {
            'start_time': TextInput(attrs={'type':'datetime-local','class':"form-control", 'placeholder':"Entry Time", 'name':"idcard_no"}),
            'end_time': TextInput(attrs={'type':'datetime-local','class':"form-control",'placeholder':"Exit Time", 'name':"address" }),
            }   
                            
    def clean(self):
        cleaned_data = super().clean()
        person = cleaned_data.get('person')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Error-Handling

        if not person:
            raise forms.ValidationError('Failed : Enter the person name')

        if not start_time:
            raise forms.ValidationError('Failed : Enter the entry time of the person')

        if not end_time:
            raise forms.ValidationError('Failed : Enter the exit time of the person')


  