from django.db import models
from django.contrib.auth.models import User
from menu.models import Menuitem


class Reviews(models.Model):

    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    class Meta:
        verbose_name_plural = 'Reviews'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review on {self.menuitem.name}"
