from django.shortcuts import render
from .forms import NewsletterForm


def newsletter(request):
    """ Signup to newsletter """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
