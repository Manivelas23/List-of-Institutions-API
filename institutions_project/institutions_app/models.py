from django.db import models

class institution(models.Model):
    name = models.CharField('Institution Name',max_length = 150)
    region = models.CharField(max_length = 100)

    def __str__(self):
        return self.name    