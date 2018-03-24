from django.shortcuts import render
from django.views import generic
# Create your views here.


from .models import Comment, Pet, User, MapPost , ServicePost , FeedPost

def index(request):
    num_pets=Pet.objects.all().count()
    return render(
        request,
        'index.html',
        context={},
    )

class Chat(generic.ListView):
    model = FeedPost

# def chat(request):
#     return render(
#         request,
#         'chat.html',
#         context={},
#     )

class Map(generic.ListView):
    model = MapPost

def map(request):
    return render(
        request,
        'map.html',
        context={},
    )

class Profile(generic.ListView):
    model = User

def profile(request):
    return render(
        request,
        'profile.html',
        context={},
    )

class Services(generic.ListView):
    model = ServicePost

# def services(request):
#     return render(
#         request,
#         'services.html',
#         context={},
#     )

def settings(request):
    return render(
        request,
        'settings.html',
        context={},
    )

