from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import MapPost

class makeServicePost(forms.Form):
    """
    requires cost, duration, name, service type.
    i think the post should have a life time of three weeks.
    """

#from mapwidgets.widgets import GoogleStaticMapWidget

class makeMapPost(forms.ModelForm):
    """
    required latitude and longitude. description and picture.
    """
    class Meta:
        model = MapPost
        fields = ('title','text','image','latitude','longitude','createdBy',)
        #need to change createdBy when ryan updates user
        #the other commented out stuff is just stuff i'm trying
        #widgets = {
        #    'longitude': GoogleStaticMapWidget,
        #    'latitude': GoogleStaticMapWidget,
        #}


class makeFeedPost(forms.Form):
    """
    here we should process a text field which will ideally write to the comment field of the feed post.
    things like the user and time or date can be provided by the views
    """