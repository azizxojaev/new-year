from django.db import models


class NewYearArticle(models.Model):
    sender_name = models.CharField(max_length=70)
    receiver_name = models.CharField(max_length=70)
    body = models.TextField()
    qr_code = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.sender_name} - {self.receiver_name}"

