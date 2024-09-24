from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import OurStory, ContactUs
from .forms import ContactUsForm


# Create your views here.
def our_story(request):
    """
    Displays the 'Our Story' page.

    ***Context***

    ``our_story``
        The OurStory object containing the content of the 'Our Story' page.

    ***Template***
    :template: our_story/our-story.html
    """

    try:
        queryset = OurStory.objects.all()
        our_story = get_object_or_404(queryset)
        return render(
            request,
            'our_story/our-story.html',
            {"our_story": our_story},
            )

    except OurStory.DoesNotExist:
        messages.error(request, 'Our Story content is not available at the moment.')
        return redirect('home')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('home')


def contact_us(request):
    """
    Handles the 'Contact Us' form submission.

    ***Context***

    ``contact_us_form``
        The form used to submit the contact us message.

    ***Template***
    :template: our_story/contact-us.html
    """

    try:
        if request.method == 'POST':
            contact_us_form = ContactUsForm(request.POST)
            if contact_us_form.is_valid():
                contact_us_form.save()
                messages.success(
                    request,
                    "Your message has been sent successfully. We try to get back to you with 2 working days. Thank you!"
                )
                return redirect('contact_us')
            else:
                messages.error(
                    request, 
                    "There was an error sending your message. Please try again."
                )
        contact_us_form = ContactUsForm()
        return render(
            request,
            'our_story/contact-us.html',
            {"contact_us_form": contact_us_form},
            )

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('contact_us')


def privacy(request):
    """
    Displays the Privacy Policy page.

    ***Template***
    :template: our_story/privacy.html
    """
    return render(
        request,
        'our_story/privacy.html',
        )
