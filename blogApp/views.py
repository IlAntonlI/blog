from django.views.generic import ListView, DetailView

from .forms import CommentModelForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blogApp/article_list.html'
    ordering = ['pub_date']
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blogApp/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentModelForm(initial={'article': self.object.pk})
        return context
