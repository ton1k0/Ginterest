from django.utils import timezone
from django.db import models
from authentication.models import User



class Gin(models.Model):
    id = models.AutoField(primary_key=True)
    #image = models.ImageField(upload_to='images/')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')


    def __str__(self):
        return self.id


    class Meta:
        verbose_name = 'Джины'
        verbose_name_plural = 'Джины'
