from django.db import models
from django.contrib.auth.models import User

class Blog_post (models.Model):
 title = models.CharField(max_length = 50)
 text = models.TextField()
 release_date = models.DateField(auto_now=False, auto_now_add=True)
 update_time = models.DateField(auto_now=True, auto_now_add=False)
 author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
 id = models.AutoField(primary_key=True)
