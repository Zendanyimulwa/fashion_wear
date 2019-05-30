from django.shortcuts import render,get_object_or_404, redirect
from . models import Clothe
from . forms import ClotheForm,UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    clothes =Clothe.objects.all()
    return render(request, 'fashionapp/index.html', {'clothes':clothes})


def details(request,Clothe_id):
        clothe = get_object_or_404(Clothe, pk= Clothe_id)
        return render(request,'fashionapp/detail.html',{'Clothe': clothe})



@login_required(login_url='fashionapp:login_user')
def create_clothe(request):
    form = ClotheForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        clothe = form.save(commit=False)
        clothe.cover = request.FILES['cover']
        clothe.user = request.user
        clothe.save()
        return redirect('fashionapp:index')
    form = ClotheForm()
    return render(request, 'fashionapp/create_clothe.html', {'form':form})


def delete_clothe(request, clothe_id):
    clothe= Clothe.objects.get(pk=clothe_id)
    clothe.delete()
    return redirect('fashionapp:index')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form . cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username = username,password=password)
        if user is not None:
            if user. is_active:
                login(request,user)
                clothes = Clothe.objects.filter(user=request.user)
            return render( request,'fashionapp/index.html',{'clothes':clothes})
    return render(request,'fashionapp/register.html',{'form':form})



def login_user(request):
    if request .method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('fashionapp:index')
    return render(request, 'fashionapp/login.html')


def logout_user(request):
    logout(request)
    return redirect('fashionapp:login_user')

