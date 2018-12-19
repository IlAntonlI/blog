from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    short_text = models.TextField(max_length=400)
    full_text = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.headline


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
