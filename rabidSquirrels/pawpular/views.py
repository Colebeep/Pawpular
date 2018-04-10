from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
import datetime

# Create your views here.

from .models import Comment, Pet, User, MapPost , ServicePost , FeedPost

@login_required
def index(request):
    num_pets=Pet.objects.all().count()
    return render(
        request,
        'index.html',
        context={},
    )

class Chat(generic.ListView):
    model = FeedPost

class Map(generic.ListView):
    model = MapPost

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
class Services(generic.ListView):
    model = ServicePost

def settings(request):
    return render(
        request,
        'settings.html',
        context={},
    )

