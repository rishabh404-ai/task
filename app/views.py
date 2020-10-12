from django.shortcuts import render, redirect
from .models import Register, Entry
from .forms import RegisterForm, RecordEntryForm
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
            return redirect('/api/v1/entry/')
      
        return render(request,self.template_name,{'form':form})  

class RecordEntryView(View):
    template_name = 'entry.html'
    form_class = RecordEntryForm

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form})


    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            entry = Entry.objects.create(
                           person=cleaned_data['person'],start_time=cleaned_data['start_time'],end_time=cleaned_data['end_time'])

            entry.save()
            return render(request,'done.html')
      
        return render(request,self.template_name,{'form':form})  






