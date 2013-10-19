from django.db import models

class Plot(models.Model):
    crop = models.CharField(max_length=200)

    def __unicode__(self):
    	return self.crop

class Organization(models.Model):
    name = models.CharField(max_length=200)
    plots = models.ForeignKey(Plot)
    
    def __unicode__(self):
    	return self.name
