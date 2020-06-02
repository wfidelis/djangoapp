from django.shortcuts import render,redirect
from .form import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('New User Created! Log In To Get Started!'))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {"register_form": register_form})
