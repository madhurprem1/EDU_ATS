from django.db import models

# Create your models here.

class index():
    pass
class login():
    pass
class about(models.Model):
    subject = models.CharField(max_length=200)
    from_email = models.CharField(max_length=200)
    message = models.CharField(max_length=500)

