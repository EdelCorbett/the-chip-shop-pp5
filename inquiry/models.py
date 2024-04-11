from django.db import models


class Inquiry(models.Model):

    class Meta:
        verbose_name_plural = 'Inquiries'

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
