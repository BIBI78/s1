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
        fields = ['title', 'content', 'kilometers_ran','location', 'duration', 'featured_image']  

  
    kilometers_ran = forms.DecimalField(label='Kilometers Ran', required=True)
    location = forms.CharField(max_length=100, label='Location', required=True)
    duration = forms.DurationField(label='Duration', required=True)
    featured_image = forms.ImageField(label='Featured Image', required=False)


# attempts update and delete user profile 
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'city', 'bio', 'profile_picture']
