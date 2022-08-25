from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi1w8yH2ByuFd22laS-H18DwU4opeldOlie9km99bFwQ&s', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.image.path)
