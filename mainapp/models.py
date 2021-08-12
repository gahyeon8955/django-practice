from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    photo = models.ImageField(upload_to="image", blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return str(self.body)[:100]