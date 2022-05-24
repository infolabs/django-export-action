# -- encoding: UTF-8 --
from six import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Publication(models.Model):
    title = models.CharField(max_length=30, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('pk',)


@python_2_unicode_compatible
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


@python_2_unicode_compatible
class Article(models.Model):
    STATUS = (
        (1, 'Draft'),
        (2, 'Revision'),
        (3, 'Published'),
    )

    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    tags = models.ManyToManyField(Tag, through='ArticleTag')
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

    @property
    def contact(self):
        return self.reporter.email


@python_2_unicode_compatible
class ArticleTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    created_on = models.DateTimeField('created on', auto_now_add=True)

    def __str__(self):
        return "{} on {}".format(self.tag, self.article)

    class Meta:
        ordering = ('created_on',)
