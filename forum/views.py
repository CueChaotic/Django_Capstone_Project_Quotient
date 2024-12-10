from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import * 
from .forms import * 

# All views
def forum_page(request):
    '''
    Collects FORUM and related DISCUSSION object data and renders it to the
    forum_page.html template.
    '''
    forums = Forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())
    context = {"forums": forums,
              "count": count,
              "discussions": discussions}
    return render(request, "forum_page.html", context)


@login_required(login_url="/user_auth")
def addInForum(request):
    '''
    Restricted view to add a forum topic, using the CreateInForum form and
    rendered in the addInForum.html template.
    '''
    form = CreateInForum()
    if request.method == "POST":
        form = CreateInForum(request.POST)
        if form.is_valid():
            forum_instance = form.save(commit = False)
            forum_instance.user = request.user
            forum_instance.save()
            form.save()
            return redirect("disc_forum:addInForum")
    context = {"form": form}
    return render(request, "addInForum.html", context)


@login_required(login_url="/user_auth")
def addInDiscussion(request):
    '''
    Restricted view to add a discussion to a forum topic, using the
    CreateInDiscussion form and rendered in the addInDiscussion.html template.
    '''
    form = CreateInDiscussion()
    if request.method == "POST":
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            discussion_instance = form.save(commit = False)
            discussion_instance.user = request.user
            discussion_instance.save()
            form.save()
            return redirect("disc_forum:addInDiscussion")
    context = {"form": form}
    return render(request, "addInDiscussion.html", context)

# NOTE: Above code to build a discussion forum sourced (before changes) from
# DataFlair:
# https://data-flair.training/blogs/discussion-forum-python-django/

