from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import OurStory, ContactUs
from .forms import ContactUsForm

# Create your views here.
def our_story(request):

    queryset = OurStory.objects.all()
    our_story = get_object_or_404(queryset)
    return render(
        request,
        'our_story/our-story.html',
        {"our_story": our_story},
        )

def contact_us(request):

    if request.method == 'POST':
        contact_us_form = ContactUsForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your message has been sent successfully. We try to get back to you with 2 working days. Thank you!"
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                "There was an error sending your message. Please try again."
            )
    contact_us_form = ContactUsForm()
    return render(
        request,
        'our_story/contact-us.html',
        {"contact_us_form": contact_us_form},
        )

def privacy(request):
    return render(
        request,
        'our_story/privacy.html',
        )