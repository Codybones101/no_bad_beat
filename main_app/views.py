from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

'''
Now we can simply “decorate” any view function that requires a user to be logged in like this:

@login_required
'''

bets = [
    {'title': 'Team A vs Team B',
        'team1': "A-Team-Value", 'team2': 'B-Team-Value', 'price': 12
     },
    {'title': 'Team C vs Team D',
        'team1': "C-Team-Value", 'team2': 'D-Team-Value', 'price': 34
     },
]


def home(request):
    return render(request, 'home.html')


@login_required
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


def bets_index(request):
    return render(request, 'bets/index.html', {
        'bets': bets
    })
