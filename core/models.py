import base64
import fixedint

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class URL(models.Model):
    long_url = models.URLField(blank=False, null=False)
    short_url = models.CharField(max_length=7)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.short_url}'


@receiver(post_save)
def on_URL_post_save(sender, instance, created, **kwargs):
    if created:
        instance.short_url = base64.urlsafe_b64encode(fixedint.Int32(hash(str(instance.id))).to_bytes()).decode('UTF-8')[:-1]
        instance.save()


class Hits(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='hits')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.url}/{self.created}'
