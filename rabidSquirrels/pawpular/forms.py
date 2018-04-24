from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

from .models import MapPost, FeedPost , ServicePost, Pet

class makeServicePost(forms.ModelForm):
    """
    requires cost, duration, name, service type.
    i think the post should have a life time of three weeks.
    """
    def clean_startDate(self):
        data = self.cleaned_data['startDate']
        #Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - date in the past'))
        # Remember to always return the cleaned data.
        return data

    def clean_endDate(self):
        data = self.cleaned_data['endDate']
        # data2 = self.cleaned_data['startDate']

        #Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - its in the past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - your service lasts longer than 4 weeks'))

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = ServicePost
        fields = ['cost','title','text','startDate','endDate']
        labels = { 'endDate': _('Ending Date'),'startDate':_('Starting Date') }
        help_texts = { 'endDate': _('Enter a date between now and 4 weeks (default 3).'), }
        

#from mapwidgets.widgets import GoogleStaticMapWidget

class makeMapPost(forms.ModelForm):
    """
    required latitude and longitude. description and picture.
    """
    class Meta:
        model = MapPost
        fields = ('title','text','image')

class makeFeedPost(forms.ModelForm):
    """
    here we should process a text field which will ideally write to the comment field of the feed post.
    things like the user and time or date can be provided by the views
    """
    class Meta:
        model = FeedPost
        fields = ('title','post','image')
        labels = { 'title': _('Post Title'),'post':_('Post Text') }


class makePet(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['name','birthday','image',]
        labels = { 'name': _('Pet Name'),'birthday':_('Pet Birthday')}