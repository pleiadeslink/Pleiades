from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Resource, Category
from .forms import CommentForm

class BlogView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'portal_blog_main.html'

def ResourceView(request):
    resources = Resource.objects.all().order_by('slug')
    return render(request, "portal_resources.html", {'resources': resources})

def PostView(request, slug):
    template_name = 'portal_blog_postview.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def TagView(request, slug):
    tag = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(tags__in=[tag]).order_by('-created_on')
    return render(request, 'portal_blog_categoryview.html', {'tag': tag, 'posts': posts})

def PostListView(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'portal_blog_postlist.html', {'posts': posts})

def AboutView(request):
    return render(request, 'portal_about.html')

def LinksView(request):
    return render(request, 'portal_links.html')