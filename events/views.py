from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Review
from .forms import ReviewForm


# Create your views here.
class Events(generic.ListView):
    """
    Returns all published events ordered by the date they were created.

    ***Context***

    ``queryset``
        All published events ordered by the date they were created.

    ***Template***
    :template: events/events.html
    """
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = "events/events.html"


def event_info(request, slug):
    """
    Displays the details of a single event.
    ***Context***

        ``event``
        The event object with the given slug.

        ``reviews``
        All reviews for the event ordered by the date they were created.

    ***Template***
    :template:events/event_info.html
    """

    try:
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        reviews = event.comments.order_by('-created_on').filter(approved=True)
        return render(request, 'events/event_info.html',
                    {'event': event, 'reviews': reviews})

    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('events')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('events')


def write_review(request, slug):
    """
    Handles the submission of a new review for an event.

    ***Context***

    ``event``
        The event object with the given slug.

    ``review_form``
        The form used to submit the review.

    ***Template***
    :template: events/event_info.html
    """

    try:
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
                messages.SUCCESS(
                    request,
                    'Review submitted successfully and awaiting approval.'
                )
                return redirect('event_info', slug=slug)
            else:
                messages.ERROR(
                    request,
                    'Review not submitted. Please try again.'
                )
        review_form = ReviewForm()
        return HttpResponseRedirect(reverse('event_info', args=[slug]))

    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('events')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('events')


def edit_review(request, slug, review_id):
    """
    Handles the editing of an existing review.

    ***Context***

    ``event``
        The event object with the given slug.

    ``review``
        The review object to be edited.

    ``review_form``
        The form used to edit the review.

    ***Template***
    :template: events/event_info.html
    """

    try:
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
                messages.SUCCESS(
                    request,
                    'Successful edit of review and after approval will be displayed.'
                    )
                return redirect('event_info', slug=slug)
            else:
                messages.ERROR(
                    request,
                    'Something went wrong. Please try to edit again.'
                )

        return HttpResponseRedirect(reverse('event_info', args=[slug]))

    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('events')

    except Review.DoesNotExist:
        messages.error(request, 'Review not found.')
        return redirect('event_info', slug=slug)

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('event_info', slug=slug)


def delete_review(request, slug, review_id):
    """
    Handles the deletion of a review.

    ***Context***

    ``event``
        The event object with the given slug.

    ``review``
        The review object to be deleted.

    ***Template***
    :template: events/event_info.html
    """

    try:
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)

        if review.author == request.user:
            review.delete()
            messages.SUCCESS(request, 'Review deleted!')
        else:
            messages.ERROR(
                request, 'You can only delete your own reviews!')

        return HttpResponseRedirect(reverse('event_info', args=[slug]))

    except Event.DoesNotExist:
        messages.error(request, 'Event not found.')
        return redirect('events')

    except Review.DoesNotExist:
        messages.error(request, 'Review not found.')
        return redirect('event_info', slug=slug)

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('event_info', slug=slug)
