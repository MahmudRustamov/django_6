from django.shortcuts import redirect, render
from django.contrib import messages
from apps.pages.forms import ContactForm


def home_view(request):
    return render(request, 'pages/home3.html')

def contact_page_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message sent successfully!")
            return redirect('pages:contact')
        else:
            return render(request, 'pages/contact.html', {'errors': form.errors})
    else:
        return render(request, 'pages/contact.html')

def about_view(request):
    return render(request, 'pages/about-us.html')

def not_found_view(request, exception=None):
    return render(request, 'pages/404.html', status=404)

