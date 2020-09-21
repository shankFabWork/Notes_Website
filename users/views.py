from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,ProfielUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} is successfully created')
            form.save()
            return redirect('login')

    else:
        form=UserRegistrationForm()

    context={'form':form}
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')


@login_required
def update(request):
    if request.method == 'POST':
        u=UserUpdateForm(request.POST,instance=request.user)
        p=ProfielUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u.is_valid() and p.is_valid():
            messages.success(request,'Form successfully updated')
            u.save()
            p.save()
            return redirect('profile')
    else:
        u=UserUpdateForm(instance=request.user)
        p=ProfielUpdateForm(instance=request.user.profile)
    context={'u_form':u,'p_form':p}
    return render(request,'users/update.html',context)
