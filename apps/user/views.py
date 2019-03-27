from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
# Create your views here.
@login_required # se necesita estar logueado para acceder a esta vista
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, tu cuenta ah sido creada!')
            return redirect('user:login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request,'home.html',{})
def logout(request):
    return render(request,'logout.html',{})