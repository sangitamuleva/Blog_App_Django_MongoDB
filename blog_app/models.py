from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)



class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_app_posts')
    status = models.IntegerField(choices=STATUS, default=0)
    mainimg=models.ImageField(upload_to='', blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.mainimg.url
        except:
            url = ''

        return url

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
