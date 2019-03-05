from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.utils import timezone

# Create your views here.
@login_required
def home(request):
    tweets = Tweet.objects.all().order_by('-pub_date')
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
            return redirect('/')
        else:
            return render(request, 'tweets/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'tweets/create.html')

@login_required
def detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = Comment.objects.filter(tweet=tweet).order_by('pub_date')
    # When form is submitted determine the type of request and complete it
    # 1 create comment, 2 edit comment, 3 delete comment, 4 private message
    if request.method == "POST":
        if request.POST.get("type") == "1":
            comment = request.POST['comment']
            comments.create(tweet=tweet, pub_date=timezone.datetime.now(), user=request.user, comment_text=comment)
        elif request.POST.get("type") == "2":
            comment = Comment.objects.get(id=int(request.POST['id']))
            comment.comment_text = request.POST['comment']
            comment.save()
        elif request.POST.get("type") == "3":
            Comment.objects.get(id=int(request.POST['id'])).delete()
        elif request.POST.get("type") == "4":             # Still need to set up messages
           Message.objects.create(message=request.POST['comment'], pub_date=timezone.datetime.now(),
                                   user_to=tweet.user, user_from=request.user, read=False)
    return render(request, 'tweets/detail.html', {'tweet':tweet, 'comments':comments})


@login_required
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
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
@login_required
def edit_post(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)

# Need Delete Comment
@login_required
def delete(request, tweet_id):
    Tweet.objects.get(id=tweet_id).delete()
    return redirect('/')

# Need Messages
