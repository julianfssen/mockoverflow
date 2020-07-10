from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import CommentForm
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}

	return render(request, 'forum/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_absolute_url(self):
    	return reverse('filtered-home', kwargs={'tags': self.tags})


class FilteredPostListView(ListView):
    model = Post
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
    	tags = self.request.GET['tags']
    	return Post.objects.filter(tags__name__in=[tags])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tags'] = self.tags
    #     return context


class PostSolvedView(DetailView):
	model = Post
	template_name = 'forum/post_detail.html'
	
	def form_valid(self, form):
		post = self.get_object()
		post.solved = True
		return super().form_valid(form)


class PostDetailView(DetailView):
	model = Post
	template_name = 'forum/post_detail.html'

	# def form_valid(self, form):
	# 	post = self.get_object()
	# 	post.solved = True
	# 	return redirect('post-detail', pk=post.pk)
	def form_valid(self, form):
		post = self.get_object()
		post.solved = True
		return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content', 'tags']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	field = ['title', 'content', 'tags']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		
		if self.request.user == post.author:
			return True
		return False


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # return redirect('post-detail', pk=post.pk)
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment_to_post.html', {'form': form})