from django.urls import path

from .views import ArticleListView, ArticleDetailView

app_name = 'blogApp'

urlpatterns = [
    path('blog/', ArticleListView.as_view(), name='article-list'),
    path('blog/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
