from django import forms


from .models import Article, Comment


class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['headline', 'short_text', 'image']


class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['article', 'name', 'email', 'text']
