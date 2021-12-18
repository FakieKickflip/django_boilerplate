from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



@login_required
@staff_member_required(login_url='/')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #save-method of UserRegisterForm returns the saved user

            #select username from the form for the message of success
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Account created for {username}')
            return redirect('login')  
    else:    
        form = UserRegisterForm()
    return render(request, "register/register.html", {"form": form})



