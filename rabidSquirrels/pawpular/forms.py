from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class makeServicePost(forms.Form):
    """
    requires cost, duration, name, service type. 
    i think the post should have a life time of three weeks.
    """


class makeMapPost(forms.Form):
    """
    required latitude and longitude. description and picture. 
    """


class makeFeedPost(forms.Form):
    """
    here we should process a text field which will ideally write to the comment field of the feed post. 
    things like the user and time or date can be provided by the views
    """