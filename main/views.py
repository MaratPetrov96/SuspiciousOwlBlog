from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from .models import Record,Comment
from .forms import AddForm,CommentForm
from django.core.paginator import Paginator
from django.views.generic import DetailView,UpdateView
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse

def main(request):
    return render(request,'main/records.html',{'data':Paginator(Record.objects.all(),2).page(1),
                                               'title':'Главная','user':request.user})

def page(request,id_):
    if id_==1:
        return redirect('main')
    return render(request,'main/records.html',{'data':Paginator(Record.objects.all(),2).page(id_),
                                               'title':'Записи','user':request.user})

def add(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    error=''
    if request.method=='POST':
        #form_ = ImageUploadForm(request.POST, request.FILES)
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error='Неверно'
    c=AddForm()
    return render(request,'main/AddForm.html',{'forma':c,'error':error,'user':request.user})

def about(request):
    return render(request,'main/BlogAbout.html',{'user':request.user})

class RecordView(DetailView):
    model=Record
    template_name='main/Record.html'
    context_object_name='record'
    #extra_context={'user':request.user}
    '''if request.method == 'POST':
        record=get_object_or_404(Record,id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.record = record
            record.comments.add(comment)
            comment.save()
            record.save()'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com'] = CommentForm
        return context

class RecordUpdate(UpdateView):
    model=Record
    template_name='main/Editor.html'
    fields=['title','anons','text']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'main/Sign.html', {'form': form,'user':request.user})

def test(request):
    return HttpResponse('<p>'+'</p><p>'.join(
        dir(Record.objects.get(id=3).comments)
        )+'</p>')
    '''return HttpResponse('<p>'+'</p><p>'.join(dir(
    get_object_or_404(Record,id=4)
        ))+'</p>')'''

def LogIn(request):
    if request.method == 'POST':
        '''form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')'''
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'main/Login.html', {'form': form,'user':request.user})

def comment(request,pk):
    if request.method == 'POST':
        record=get_object_or_404(Record,id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.record = record
            comment.save()
            record.comments.add(comment)
            record.save()
    return redirect('one',pk=pk)

def like(request,pk):
    record=get_object_or_404(Record,id=request.POST.get('like_btn'))
    if request.user.is_authenticated:
        record.likes.add(request.user)
        return HttpResponseRedirect(reverse('one',args=[str(pk)]))
    return redirect('login')

@login_required
def LogOut(request):
   logout(request)
   return redirect('main')
