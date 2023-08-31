from .models import Comment
from django import forms
from .models import Post



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Adjust this based on your model fields

    # Add any additional fields or custom validation methods here
    # For example, you can add a field for kilometers, location, and duration
    kilometers_ran = forms.DecimalField(label='Kilometers Ran', required=True)
    location = forms.CharField(max_length=100, label='Location', required=True)
    duration = forms.DurationField(label='Duration', required=True)