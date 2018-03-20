from django.shortcuts import render

# Create your views here.


from .models import Comment, Pet, User, Post

def index(request):
    return render(
        request,
        'index.html',
        context={},
    )