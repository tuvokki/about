from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.CharField(max_length=1200)
    is_current = models.BooleanField()
    def __unicode__(self):
        return self.title