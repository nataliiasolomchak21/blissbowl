from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages

from django.shortcuts import render
from .forms import ContactForm


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully")
            return redirect(reverse("contact_us"))
        else:
            messages.error(request, "Form submission failed. Please check the errors.")
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
