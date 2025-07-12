from django.shortcuts import render

# Create your views here.

#our functions below always take in a request parameter. This request is what the frontend ask for backend
#to serve to them

def post_list(request):
    return render(request, 'blog/post_list.html', {})