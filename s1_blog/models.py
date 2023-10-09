from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import timedelta

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (CharField): The title of the blog post.
        slug (SlugField): A unique slug for the blog post.
        author (ForeignKey): The author of the blog post.
        featured_image (CloudinaryField): The featured image for the blog post.
        excerpt (TextField): A brief excerpt or summary of the blog post.
        updated_on (DateTimeField): The date and time when the post was last updated.
        content (TextField): The main content of the blog post.
        created_on (DateTimeField): The date and time when the post was created.
        status (IntegerField): The status of the post (Draft or Published).
        likes (ManyToManyField): Users who liked the blog post.
        price (DecimalField): The price associated with the post.
        location (CharField): The location associated with the post.

    Methods:
        number_of_likes: Returns the number of likes for the post.

    Meta:
        ordering: Specifies the default ordering of posts by created_on.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (ForeignKey): The blog post to which the comment belongs.
        name (CharField): The name of the commenter.
        email (EmailField): The email address of the commenter.
        body (TextField): The content of the comment.
        created_on (DateTimeField): The date and time when the comment was created.
        approved (BooleanField): Indicates if the comment is approved.

    Meta:
        ordering: Specifies the default ordering of comments by created_on.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class UserProfile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (OneToOneField): The user associated with the profile.
        bio (TextField): A biography or description of the user.
        profile_picture (ImageField): The user's profile picture.
        city (CharField): The city where the user is located.
        name (CharField): The name of the user.

    Methods:
        __str__: Returns the username of the associated user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
