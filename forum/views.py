from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import * 
from .forms import * 

# All views
def forum_page(request):
    """Collects FORUM and related DISCUSSION object data and renders it to the
    forum_page.html template.

    :param request: The request object sent to the server.
    :param forums: Grabs all the Forum objects in the database.
    :param count: Counts the number of Forum objects.
    :param discussions: Initial empty list to store all the Discussion objects
        sitting in each Forum object.

    :return: The forum_page.html template with the context.
    """
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
    """Restricted view to add a forum topic, using the CreateInForum form and
    rendered in the addInForum.html template.

    :param request: The request object sent to the server.
    :param form: The CreateInForum form pulled from forms.py. Form request
        method is checked and form is saved if valid.
    :param forum_instance: The instance of the forum object created.
    :param context: The context dictionary to be rendered in the template.

    :return: The addInForum.html template with the context.
    """
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
    """Restricted view to add a discussion to a forum topic, using the
    CreateInDiscussion form and rendered in the addInDiscussion.html template.

    :param request: The request object sent to the server.
    :param form : The CreateInDiscussion form pulled from forms.py. The form
        request method is checked and form is saved if valid.
    :param discussion_instance: The instance of the discussion object that is
        created.
    :param context: The context dictionary to be rendered in the template.

    :return: The addInDiscussion.html template with the context.
    """
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
