from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog
from .forms import BlogPost
from django.db.models import Q

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'mainapp/home.html', {"blogs":blogs, 'posts':posts})

def search(request):
    blog_list = Blog.objects.all()
    b = request.GET.get('b','')
    if b:
        blog_list = blog_list.filter(
            Q(title__icontains=b) |
            Q(body__icontains=b)
        ).distinct()
    return render(request, 'mainapp/search.html', {'blog_list':blog_list, 'b':b})
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'mainapp/detail.html', {'blog':blog_detail})

# def create(request):
#     blog = Blog()
#     blog.title = request.GET['title']
#     blog.body = request.GET['body']
#     blog.photo = request.FILES.get('photo')
#     # blog.photo = request.FILES['photo']
#     blog.pub_date = timezone.datetime.now()
#     blog.save()
#     # for i in range(0,10):
#     #     blog=Blog()
#     #     blog.title=myfake.name()
#     #     blog.body=myfake.sentence()
#     #     blog.pub_date = timezone.datetime.now()
#     #     blog.save()
#     return redirect('/blog/' + str(blog.id))

# myfake = Faker()

def new(request):
    if request.method =='POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'mainapp/create.html',{'form':form})

def delete(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.delete()
    return redirect('home')

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            print(form.cleaned_data)
            blog.title = form.cleaned_data['title']
            blog.photo = form.cleaned_data['photo']
            blog.body = form.cleaned_data['body']
            blog.save()
            return redirect('/blog/' + str(blog.id))
    else:
        form = BlogPost(instance=blog)
        return render(request,'mainapp/update.html',{'form':form})

# def update(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     form = BlogPost(request.POST, request.FILES, instance=blog, auto_id=True)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("/blog/" + str(blog_id))
#     else:
#         form = BlogPost(instance=blog)
#         return render(request, 'mainapp/update.html', {"form": form})