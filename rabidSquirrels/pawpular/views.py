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
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
    # fields = ['text']
    # template_name_suffix = '_list'

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

class ServiceCreate(CreateView):
    model = ServicePost
    fields = ['text','title','cost','startDate','endDate']

from .forms import makeMapPost
from django.contrib.auth import get_user

def mappost_new(request):
    if request.method == 'POST':
        form = makeMapPost(request.POST)
        
        if form.is_valid():
            #clean data
            MapPost = form.save(commit=False)
            #MapPost.createdBy = get_user(request)
            #need to fix the above line when ryan updates user
            MapPost.createdOn = datetime.date.today()
            MapPost.expiry = datetime.date.today() + datetime.timedelta(weeks=3)
            #fix how image works maybe?
            MapPost.save()
            return HttpResponseRedirect(reverse('map'))
    else:
        form = makeMapPost()
    return render(request,'pawpular/mappost_edit.html',{'form':form, })