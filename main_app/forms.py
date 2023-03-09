from django.forms import ModelForm
from .models import Comment, Bet

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        
class BetForm(ModelForm):
    class Meta:
        model = Bet
        fields = ['bet_size']