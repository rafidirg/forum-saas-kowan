import random
import string

from authapp.models import AppUser, Course
from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymcemodels


class Post(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    content = tinymcemodels.HTMLField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) \
                        + '-p' \
                        + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = tinymcemodels.HTMLField(default="")
