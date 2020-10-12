from django.shortcuts import render
from .models import Register
from .forms import RegisterForm
from django.http import HttpResponse
from django.views import View
# Create your views here.

class RegisterView(View):
    template_name = 'index.html'
    form_class = RegisterForm

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form})


    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            register = Register.objects.create(
                           name=cleaned_data['name'],idcard_no=cleaned_data['idcard_no'],id_type=cleaned_data['id_type'],
                           address=cleaned_data['address'],phone_no=cleaned_data['phone_no'],email=cleaned_data['email'],
                           meet_with=cleaned_data['meet_with'])

            register.save()
            return HttpResponse('Response Subbmited') 
      
        return render(request,self.template_name,{'form':form})        



