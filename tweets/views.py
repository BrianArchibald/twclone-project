from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.utils import timezone

# Create your views here.
def home(request):
    tweets = Tweet.objects
    return render(request, 'tweets/home.html', {'tweets': tweets})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['tweet_text']:
            tweet = Tweet()
            tweet.tweet_text = request.POST['tweet_text']
            tweet.pub_date = timezone.datetime.now()
            tweet.user = request.user
            tweet.save()
            return redirect('/tweets/' + str(tweet.id))
        else:
            return render(request, 'tweets/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'tweets/create.html')

def detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweets/detail.html', {'tweet':tweet})


@login_required
def add_comment(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        if request.POST['comment_text']:
            comment = Comment()
            comment.comment_text = request.POST['comment_text']
            comment.pub_date = timezone.datetime.now()
            comment.user = request.user
            comment.save()
            return redirect('/tweets/' + str(tweet.id))
        else:
            return render(request, 'tweets/add_comment.html', {'error': 'All fields are required'})
    else:
        return render(request, 'tweets/add_comment.html')

# Need Edit Comment


# Need Delete Comment


