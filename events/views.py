from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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

    return render(
        request,
        'events/event_info.html',
        {'event': event,
        'reviews': reviews},)
    
def write_review(request, slug):

    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)
    review = event.comments.filter(approved=True)

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

    return HttpResponseRedirect(reverse('event_info', args=[slug]))

def edit_review(request, slug, review_id):

    if request.method == "POST":
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)
        
        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.post = event
            review.approved = False
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review updated successfully and awaits approval to be displayed.'
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Something went wrong. Please try to edit again.'
            )

    return HttpResponseRedirect(reverse('event_info', args=[slug]))

def delete_review(request, slug, review_id):

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_info', args=[slug]))