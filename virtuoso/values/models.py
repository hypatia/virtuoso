from django.db import models

class Value(models.Model):
    value = models.CharField(max_length=300,blank=False)
    frequency = models.IntegerField(default=0)

    def __unicode__(self):
        return self.value
        
