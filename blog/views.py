from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.


#our functions below always take in a request parameter. This request is what the frontend ask for backend
#to serve to them

def post_list(request):
    Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': Posts})