from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import Event, Review
from .forms import ReviewForm

# Create your views here.
class Events(generic.ListView):
    queryset = Event.objects.all()
    template_name = "events/events.html"


def event_info(request, slug):

    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)
    reviews = event.comments.order_by('-created_on').filter(approved=True)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.post = event
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted successfully and awaiting approval.'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Review not submitted. Please try again.'
            )
    review_form = ReviewForm()

    return render(
        request,
        'events/event_info.html',
        {'event': event,
        'reviews': reviews,
        'review_form': review_form},)