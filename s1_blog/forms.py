from django import forms
from .models import Comment, Post, UserProfile

class CommentForm(forms.ModelForm):
    """
    Form for creating a new comment.

    Attributes:
        body (CharField): Text area for the comment's body.
    """

    body = forms.CharField(
        label='',  # Set an empty label
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})  # Adjust rows and cols as needed
    )

    class Meta:
        model = Comment
        fields = ['body']

class CreatePostForm(forms.ModelForm):
    """
    Form for creating a new post.

    Attributes:
        location (CharField): Location for the post.
        price (DecimalField): Price for the post.
        featured_image (ImageField): Featured image for the post.
    """

    class Meta:
        model = Post
        fields = ['title', 'content', 'location', 'price', 'featured_image']

    location = forms.CharField(max_length=100, label='Location', required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price', required=True)
    featured_image = forms.ImageField(label='Featured Image', required=False)

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Attributes:
        name (CharField): User's name.
        city (CharField): User's city.
        bio (CharField): User's biography.
        profile_picture (ImageField): User's profile picture.
    """

    class Meta:
        model = UserProfile
        fields = ['name', 'city', 'bio', 'profile_picture']
