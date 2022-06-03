import uuid
from django.db import models
from .utils import create_short_url

class ShortenerItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ['-created']
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_short_url(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.long_url}-{self.short_url}'
