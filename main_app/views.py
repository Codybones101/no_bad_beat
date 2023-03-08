from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Comment
from .forms import CommentForm
from django.views.generic.edit import UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            # <--------------------------------------- We need to change this
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {
        'games': games
    })


@login_required
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    comment_form = CommentForm()
    return render(request, 'games/detail.html', {
        'game': game, 'comment_form': comment_form
    })


@login_required
def add_comment(request, game_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.comment_user = request.user
        new_comment.game_id = game_id
        new_comment.save()
    return redirect('detail', game_id=game_id)


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['comment']
    success_url = '/games/{game_id}'


class CommentDelete(DeleteView):
    model = Comment
    success_url = '/games/{game_id}'
