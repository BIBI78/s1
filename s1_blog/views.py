from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, redirect
from .forms import CreatePostForm
from django.urls import reverse_lazy

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


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
                "comment_form": CommentForm()
            },
        )
     # commenty
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
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


from django.views.generic.edit import CreateView
from .models import Post

 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Post
from .forms import CreatePostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


from django.utils.text import slugify

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            # Generate a unique slug based on the post title
            base_slug = slugify(post.title)
            unique_slug = base_slug
            num = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            
            post.slug = unique_slug
            post.save()
            return redirect('home')
    else:
        form = CreatePostForm()
    
    return render(request, 'create_post.html', {'form': form})



# from django.views.generic.edit import UpdateView
# from .models import Post
# from .forms import CreatePostForm

# class PostUpdateView(UpdateView):
#     model = Post
#     form_class = CreatePostForm
#     template_name = 'update_post.html' 
#     success_url = reverse_lazy('home')  

# #Delete post

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import DeleteView
# from .models import Post
# from django.urls import reverse_lazy

# class PostDeleteView(LoginRequiredMixin,DeleteView):
#     model = Post
#     template_name = 'delete_post.html'  
#     success_url = reverse_lazy('home')  
######
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            # Redirect to a page or show a message indicating that the user can't delete this post.
            # You can customize this part as per your requirements.
            return HttpResponseForbidden("You don't have permission to delete this post.")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content']  # Fields that can be edited by the user.
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            # Redirect to a page or show a message indicating that the user can't edit this post.
            # You can customize this part as per your requirements.
            return HttpResponseForbidden("You don't have permission to edit this post.")


#####

# user profile blah blah blah 

# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.models import User
# from .models import UserProfile

# def user_profile(request, username):
#     # Retrieve the user by username
#     user = get_object_or_404(User, username=username)

#     # Retrieve the user's profile
#     user_profile = user.userprofile

#     return render(
#         request,
#         'user_profile.html',
#         {'user': user, 'user_profile': user_profile}
#     )


#test user profile update and delete 
# 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# @login_required
# def update_profile(request):
#     user_profile = get_object_or_404(UserProfile, user=request.user)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('user_profile')
#     else:
#         form = UserProfileForm(instance=user_profile)

#     return render(request, 'update_profile.html', {'form': form})
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def update_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()

            # Redirect to the updated user profile page
            return redirect(reverse('user_profile', kwargs={'username': request.user.username}))
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'update_profile.html', {'form': form})


@login_required
def delete_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        user_profile.delete()
        return redirect('home')  # Redirect to the home page or another suitable URL

    return render(request, 'delete_profile.html', {'user_profile': user_profile})


#test

# registerrrr

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import UserProfile  # Import the UserProfile model

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile instance for the user
            UserProfile.objects.create(user=user)
            # Log the user in
            login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

####
# user profile 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def user_profile(request, username):
    # Retrieve the user by username
    user = get_object_or_404(User, username=username)

    # Retrieve the user's profile (if you have a UserProfile model)
    # user_profile = user.userprofile  # Uncomment if you have a UserProfile model

    # Retrieve the user's posts
    user_posts = Post.objects.filter(author=user)

    return render(
        request,
        'user_profile.html',
        {'user': user, 'user_posts': user_posts}
    )
