from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default_ot0aze.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 150 or img.width > 150:
    #         output_size = (150, 150)
    #         img.thumbnail(output_size)
    #         # img.save(self.image.path)
    #         img.save(self.image.name)
    #         # Remove the original pic
    #         # os.remove(self.image.path)
