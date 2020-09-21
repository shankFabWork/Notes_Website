from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import PostUpdateForm,PostCreateForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'pages/home.html')

@login_required
def update_post(request,id):
    user=User.objects.filter(username=request.user).first()
    data=Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST,instance=data)
        if form.is_valid():
            messages.success(request,'Post Updated Successfully')
            form.save()
            return redirect('all_post')

    else: 
        form = PostUpdateForm(instance=data)


    context={'data':data,'form':form}
    return render(request,'pages/update_post.html',context)

@login_required
def delete_post(request,id):
    user=User.objects.filter(username=request.user).first()
    data=Post.objects.get(id=id)
    data.delete()
    return redirect('home')


@login_required
def create_post(request):
    user=User.objects.filter(username=request.user).first()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            messages.success(request,'Post created Sucessfully')
            f=form.save(commit=False)
            f.user=request.user
            f.save()
            return redirect('all_post')
    else:
        form = PostCreateForm(instance=request.user)
        context={'form':form}
        return render(request,'pages/create_post.html',context)


@login_required
def all_post(request):
    user=User.objects.filter(username=request.user).first()
    arr=Post.objects.filter(user=user)
    context={'arr':arr}
    return render(request,'pages/all_post.html',context)


@login_required
def search_post(request):
    title=request.GET.get('search')
    print(title)
    arr=[]
    if title != None:
        arr=Post.objects.filter(title__icontains=title,user=request.user)
    context={'arr':arr}
    print(arr)        
    return render(request,"pages/search_post.html",context)


@login_required
def global_post(request):
    if request.user.is_superuser:
        arr=User.objects.all()
        context={'arr':arr}
    else:
        data='You are not a super user'
        context={'data':data}

    return render(request,"pages/global_post.html",context)
