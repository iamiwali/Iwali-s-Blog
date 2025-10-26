from django import forms
from .models import Story, Subscriber

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'email-input'
            }),
        }
