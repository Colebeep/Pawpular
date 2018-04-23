from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.urls import reverse
import datetime
from django import template

# Create your views here.

from .models import Comment, Pet, Profile, MapPost , ServicePost , FeedPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView


register = template.Library()

@login_required
def index(request):
    num_pets=Pet.objects.all().count()
    return render(
        request,
        'index.html',
        context={},
    )


class Chat(LoginRequiredMixin, generic.ListView):
    model = FeedPost
    # fields = ['text']
    # template_name_suffix = '_list'
    def chat(request):
        return render(
            request,
            'pawpular/feedpost_list.html'
        )

class Map(LoginRequiredMixin, generic.ListView):
    model = MapPost

class profile_detail_view(LoginRequiredMixin, generic.DetailView):
    model = Profile
        
    def profile_detail_view(self, request, pk):

        user = Profile.objects.get(pk=pk)
        pet_amount = Profile.pets.all().length()
        return render(
            request,
            'pawpular/user_detail.html',
            context={'user':user, 'pet_amount': pet_amount}
        )
class Services(LoginRequiredMixin, generic.ListView):
    model = ServicePost

@login_required
def settings(request):
    return render(
        request,
        'settings.html',
        context={},
    )

class ServiceCreate(CreateView):
    model = ServicePost
    fields = ['text','title','cost','startDate','endDate']


from .forms import makeMapPost , makeFeedPost , makeServicePost
from django.contrib.auth import get_user

@register.inclusion_tag("pawpular/mappost_list.html", takes_context=True)
def mappost_new(request, lat, lon):
    if request.method == 'POST':
        form = makeMapPost(request.POST, request.FILES)
        if form.is_valid():
            #clean data
            MapPost = form.save(commit=False)
            MapPost.createdBy = request.user.profile
            MapPost.createdOn = datetime.date.today()
            MapPost.expiry = datetime.date.today() + datetime.timedelta(weeks=3)
            MapPost.latitude = lat
            MapPost.longitude = lon
            MapPost.save()
            return HttpResponseRedirect(reverse('map'))
    else:
        form = makeMapPost()
    return render(request,'pawpular/mappost_edit.html',{'form':form})


def feedpost_new(request):
    if request.method == 'POST':
        form = makeFeedPost(request.POST, request.FILES)

        if form.is_valid():
            FeedPost = form.save(commit=False)
            FeedPost.createdBy = request.user.profile
            FeedPost.createdOn = datetime.date.today()
            FeedPost.expiry = datetime.date.today() + datetime.timedelta(weeks=3)
            FeedPost.save()
            return HttpResponseRedirect(reverse('chat'))
    else:
        form = makeFeedPost(request.POST)
    return render(request,'pawpular/feedpost_new.html',{'form':form, })
        
def create_new_service(request):
    if request.method == 'POST':
        form = makeServicePost(request.POST)

        if(form.is_valid()):
            service = form.save(commit = False)
            service.createdOn = datetime.date.today()
            service.createdBy = request.user.profile
            service.startDate = datetime.date.today()
            service.endDateg = datetime.date.today() + datetime.timedelta(weeks=3)

            service.save()
            return HttpResponseRedirect(reverse('services'))
    else:
       form=makeServicePost() 
    return render(request,'pawpular/servicepost_form.html',{'form':form, })

@register.inclusion_tag("pawpular/feedpost_edit.html", takes_context=True)
def feedpost_edit(request, id):
    if id:
        feedpost = get_object_or_404(FeedPost, pk=id)
    
        if feedpost.createdBy != request.user.profile:
            print('createdBy mismatch')
            return HttpResponseForbidden()
    else:
        feedpost = FeedPost(createdBy=request.user.profile)

    form = makeFeedPost(request.POST, request.FILES, instance=feedpost)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        return HttpResponseRedirect(reverse('chat'))

    return render(request, 'pawpular/feedpost_edit.html', {'form':form, })
