from .models import Comment
from django import forms
from .models import Post
from django import forms
from .models import UserProfile



# class CommentForm(forms.ModelForm):
#     body = forms.CharField(label='')

#     class Meta:
#         model = Comment
#         fields = ('body',)
class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label='',  # Set an empty label
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})  # Adjust rows and cols as needed
    )

    class Meta:
        model = Comment
        fields = ['body']



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'kilometers_ran','location', 'duration', 'featured_image']  

  
    kilometers_ran = forms.DecimalField(label='Kilometers Ran', required=True)
    location = forms.CharField(max_length=100, label='Location', required=True)
    duration = forms.DurationField(label='Duration', required=True)
    featured_image = forms.ImageField(label='Featured Image', required=False)





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'city', 'bio', 'profile_picture']


