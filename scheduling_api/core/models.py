from django.db import models

# Create your models here.


class ScheduleCall(models.Model):
    site_url = models.URLField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.site_url
        