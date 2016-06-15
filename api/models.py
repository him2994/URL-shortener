from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Main(models.Model):
	surl = models.CharField(max_length=1000)
	furl = models.CharField(max_length=1000)
