from django.utils import timezone
from django.db import models



class Gin(models.Model):
    gin_id = models.AutoField(primary_key=True)
    #gin_image = models.ImageField(upload_to='images/')
    gin_description = models.TextField()
    gin_created_at = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.gin_id

    class Meta:
        verbose_name = 'Джины'
        verbose_name_plural = 'Джины'
