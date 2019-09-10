from django.views.generic import DetailView, ListView, TemplateView
from .models import Post
from series.models import Series
import markdown

from django.db.models import Count

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.latest('published_on')
        context["series"] = Post.objects.filter(series=context["post"].series) \
                .values_list('id', 'title', 'published_on', 'slug')
        return context
    


class PostDetailView(DetailView):
    template_name = 'post/detail.html'
    model = Post
    lookup_field = 'slug'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = Post.objects.filter(series=self.get_object().series) \
        .values_list('id', 'title', 'published_on', 'slug')
        return context
    

class Archive(TemplateView):
    template_name = 'post/archive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('slug', False)

        if slug:
            context["posts"] = Post.objects.filter(series__slug=slug).values_list('published_on', 'slug', 'title', 'series__name')
        elif self.request.GET.get('filter', 'posts') == 'posts':
            context["posts"] = Post.objects.values_list('published_on', 'slug', 'title')
        else:
            context["series"] = Series.objects.values_list('slug', 'name', 'timestamp').annotate(post_count=Count('post'))

        
        return context
    
    