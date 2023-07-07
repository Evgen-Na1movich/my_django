from django.db import models


class Sity(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Automat(models.Model):
    sity = models.ForeignKey(
        Sity,
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='sities'
    )
    street = models.CharField(max_length=50)
    time_service = models.DateTimeField(auto_now_add=True)
