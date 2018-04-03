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

# def map(request):
#     return render(
#         request,
#         'map.html',
#         context={},
#     )

class Profile(generic.DetailView):
    model = User
        
    def profile(self, request, pk): 

        user = User.objects.get(pk=pk)
        pet_amount = user.pets.all().length()
        return render(
            request,
            'pawpular/user_detail.html',
            context={'user':user, 'pet_amount': pet_amount}
        )
# def profile(request):
#     return render(
#         request,
#         'profile.html',
#         context={},
#     )

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

