from django.db import models


class Post(models.Model):
    idpost = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    datepost = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.CharField(max_length=1000)
    active = models.BooleanField(default=1)

    def __str__(self):
        return self.text

    class Meta:
        managed = False
        db_table = 'post'

