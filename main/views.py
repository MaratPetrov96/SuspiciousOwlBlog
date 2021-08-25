from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Record
from .forms import AddForm
from django.core.paginator import Paginator
from django.views.generic import DetailView

def main(request):
    return render(request,'main/records.html',{'data':Paginator(Record.objects.all(),2).page(1),
                                               'title':'Главная'})

def page(request,id_):
    if id_==1:
        return redirect('main')
    return render(request,'main/records.html',{'data':Paginator(Record.objects.all(),2).page(id_),
                                               'title':'Записи'})

def add(request):
    error=''
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error='Неверно'
    c=AddForm()
    return render(request,'AddForm.html',{'error':error})

def about(request):
    return render(request,'main/BlogAbout.html')

class RecordView(DetailView):
    model=Record
    template_name='main/Record.html'
    context_object_name='record'

# Create your views here.
