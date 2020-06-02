from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from blog.models import BlogPost
from blog.form import BlogForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
            'welcome_text': 'Welcome to the home page. View some more stuff soon'
            }
    return render(request,'index.html', context)

@login_required
def blogpost(request):
    all_blogs = BlogPost.objects.filter(manager = request.user)
    if request.method == "POST":
        form = BlogForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request, ('New Task Added!'))
            return redirect('blogpost')
    else:
        form = BlogForm()
        paginator = Paginator(all_blogs, 5)
        page = request.GET.get('pg')
        all_blogs = paginator.get_page(page)

    return render(request, 'blog.html',{'form':form, 'all_blogs': all_blogs } )

def contact(request):
    context = {
            'contact_text': 'welcome to my contacts page.\n If you have any issues call : 0700000000!'
            }
    return render(request, 'contact.html', context)

def about(request):
    context = {
            'about_text': 'i do a whole lot of stuff but since it doesn\'t matter just deal with this.!'
            }
    return render(request, 'about.html', context)

@login_required
def delete_task(request, task_id):
    one_blog = BlogPost.objects.get(pk=task_id)
    if one_blog.manager == request.user:
        one_blog.delete()
    else:
        messages.error(request, ('Error acessing this funtionality. Check your user and try again'))
    return redirect('blogpost')

@login_required
def edit_task(request, task_id):
    blog_object = BlogPost.objects.get(pk=task_id)

    if request.method == "POST":
        form = BlogForm(request.POST or None, instance = blog_object)
        if form.is_valid():
            form.save()
            messages.success(request, ('Task edited!'))
            return redirect('blogpost')
    else:
        return render(request, 'edit.html',{'blog_object': blog_object } )

@login_required
def complete_task(request, task_id):
    blog = BlogPost.objects.get(pk=task_id)
    if blog.manager == request.user:
        blog.done = True
        blog.save()
    else:
        messages.error(request, ('Error acessing this funtionality. Check your user and try again'))
        
    return redirect('blogpost')

@login_required
def pending_task(request, task_id):
    blog = BlogPost.objects.get(pk=task_id)
    blog.done = False
    blog.save()

    return redirect('blogpost')

