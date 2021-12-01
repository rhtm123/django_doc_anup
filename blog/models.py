from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog", null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
