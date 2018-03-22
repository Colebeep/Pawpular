from django.shortcuts import render

# Create your views here.


from .models import Comment, Pet, User, Post

def index(request):
    num_pets=Pet.objects.all().count()
    return render(
        request,
        'index.html',
        context={},
    )

def chat(request):
    return render(
        request,
        'chat.html',
        context={},
    )

def map(request):
    return render(
        request,
        'map.html',
        context={},
    )

def profile(request):
    return render(
        request,
        'profile.html',
        context={},
    )

def services(request):
    return render(
        request,
        'services.html',
        context={},
    )

def settings(request):
    return render(
        request,
        'settings.html',
        context={},
    )

