from django.db import models
from django.utils import timezone
from authentication.models import User
from gin.models import Gin

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    gin = models.ForeignKey(Gin, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='user')

