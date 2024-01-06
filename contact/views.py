from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib  import messages

from django.shortcuts import render
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
           
        messages.success(request, "Your message was sent successfully")
        return redirect('contact_us')  
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

