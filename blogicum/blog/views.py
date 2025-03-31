from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone
from blog.models import Post, Category
from django.http import Http404


class HomePageView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )[:5]
        return context


class CategoryPostsView(ListView):
    model = Post
    template_name = 'blog/category.html'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs.get('slug')
        )
        if not self.category.is_published:
            raise Http404("Категория не опубликована")
        return Post.objects.filter(
            category=self.category,
            is_published=True,
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if not post.is_published:
            raise Http404("Публикация не опубликована")
        if not post.category.is_published:
            raise Http404("Категория публикации не опубликована")
        if post.pub_date > timezone.now():
            raise Http404("Публикация еще не опубликована")
        return post
