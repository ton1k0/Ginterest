from django.db import models
from authentication.models import User


class Profile(models.Model):
    #avatar = models.ImageField(upload_to='images/')
    user = models.OneToOneField(User, verbose_name="Пользователь", related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    about = models.CharField(max_length=500)
    website = models.TextField()
    username = models.CharField(db_index=True, max_length=255, unique=True)


