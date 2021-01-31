from django.views import generic
from .models import Article

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Article
    paginate_by = 5

    def get_queryset(self):
        articles = Article.objects.order_by('-created_at')
        return articles

class DetailView(generic.DetailView):
    model = Article
    slug_field = 'title'
    slug_url_kwarg = 'title'

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'