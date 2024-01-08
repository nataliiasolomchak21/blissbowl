from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Newsletter
from .forms import NewsletterForm

def newsletter(request):
    """ Signup to newsletter """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if the email is not already subscribed
            if not Newsletter.objects.filter(email=email).exists():
                # Save the email to the database
                newsletter = Newsletter(email=email)
                newsletter.save()

                # Send confirmation email
                send_confirmation_email(email)

                messages.success(request, 'You have successfully subscribed to our newsletter!')
            else:
                messages.warning(request, 'This email is already subscribed to our newsletter.')
            
            return redirect('base') 

    else:
        form = NewsletterForm()

    return render(request, 'base.html', {'form': form})

def send_confirmation_email(email):
    """Send newsletter signup confirmation email"""
    subject = render_to_string(
                'newsletter/welcome_newsletter_subject.txt')
    message = render_to_string('newsletter/welcome_newsletter_subject.txt', {'email': email})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
