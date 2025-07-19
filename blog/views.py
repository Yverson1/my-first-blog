from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.


#our functions below always take in a request parameter. This request is what the frontend ask for backend
#to serve to them

def post_list(request):
    Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': Posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
    
     form = PostForm(request.POST)
     if form.is_valid():
        post = form.save( commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
   post = get_object_or_404(Post, pk=pk)
   if request.method == "POST":
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
           form.save()
           return redirect('post_detail', pk=post.pk)
   else:
       form = PostForm(instance=post)
   return render(request, 'blog/post_edit.html', {'form': form})