from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, UserProfile
from .forms import CommentForm, CreatePostForm, UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = False

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            base_slug = slugify(post.title)
            unique_slug = base_slug
            num = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            post.slug = unique_slug
            post.save()
            return redirect("home")
    else:
        form = CreatePostForm()

    return render(request, "create_post.html", {"form": form})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to delete this post.")




class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["title", "content"]

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to edit this post.")

    def get_success_url(self):
        # Redirect to the detail page of the updated post using its slug
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


@login_required
def delete_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        user_profile.delete()
        return redirect("home")

    return render(request, "delete_profile.html", {"user_profile": user_profile})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("profile", username=user.username)
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user)

    return render(
        request, "user_profile.html", {"user": user, "user_posts": user_posts}
    )



@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if the user who is currently logged in is the author of the comment
    if comment.name == request.user.username:
        comment.delete()
        
        # Redirect back to the previous page or a default page
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer or 'home')  # Replace 'home' with your desired default URL pattern
    
    else:
        return redirect("unauthorized")


# attempt at infinite scroll

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 100

from django.http import JsonResponse
from .models import Post

def get_paginated_posts(request, page_number):
    # Calculate the starting and ending index for the posts based on the page number.
    per_page = 100
    start_index = (page_number - 1) * per_page
    end_index = page_number * per_page

    # Retrieve the posts from the database.
    posts = Post.objects.filter(status=1).order_by("-created_on")[start_index:end_index]

    # Serialize the posts to JSON.
    serialized_posts = [{'title': post.title, 'content': post.content} for post in posts]

    return JsonResponse({'posts': serialized_posts})


# UPDATE USER PROFILE 


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user)

    return render(
        request, "user_profile.html", {"user": user, "user_posts": user_posts}
    )


from django.urls import reverse_lazy
from django.shortcuts import redirect

@login_required
def update_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            if user_profile is None:
                # Create a new UserProfile object if it doesn't exist
                user_profile = form.save(commit=False)
                user_profile.user = request.user
                user_profile.save()
            else:
                form.save()
            # Redirect to the user's profile page
            return redirect('user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "update_profile.html", {"form": form})

# About page

def about_view(request):
    # Your view logic for the 'about' page
    return render(request, 'about.html')



# Artists page

from django.shortcuts import render
from django.contrib.auth.models import User

def artists_view(request):
    # Get all users (artists)
    artists = User.objects.all()

    return render(
        request, "artists.html", {"artists": artists}
    )
