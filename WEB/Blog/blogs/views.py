from django.shortcuts import render,redirect

from .models import BlogPost

from .forms import BlogForm

from django.http import Http404

from django.contrib.auth.decorators import login_required


# Create your views here.

def confirm_user(request,blog):
    if request.user != blog.owner:
        raise Http404 

def index(request):
    blogs = BlogPost.objects.order_by('-date_add')
    context = {"blogs": blogs}
    return render(request, 'blogs/index.html', context)

def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog':blog}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            form.save()
            return redirect('blogs:index')
    
    context = {'form':form}
    return render(request, 'blogs/new_blog.html', context)

def edit_blog(request,blog_id):
    blog = BlogPost.objects.get(id = blog_id)
    confirm_user(request, blog)
    
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    
    context = {'form':form,'blog':blog}
    return render(request, 'blogs/edit_blog.html', context)

