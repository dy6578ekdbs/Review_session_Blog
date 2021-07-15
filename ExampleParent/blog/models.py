from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #<!----- 이거 그냥 어드민에 보여줄 때의 이름인듯
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
