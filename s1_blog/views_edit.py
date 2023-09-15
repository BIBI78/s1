from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.urls import reverse_lazy
from .models import Comment
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse
from .forms import UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, redirect




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
     # comment
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

   
    user_posts = Post.objects.filter(author=user)

    return render(
        request,
        'user_profile.html',
        {'user': user, 'user_posts': user_posts}
    )






@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Check if the user is the author of the comment
    if comment.user == request.user:
        comment.delete()
        # Redirect to a success page or the comment list
        return redirect('comment_list')  # Replace 'comment_list' with your desired URL name
    else:
        # Handle unauthorized deletion (e.g., show an error message)
        return redirect('unauthorized')  # Replace 'unauthorized' with an appropriate URL name for unauthorized access
