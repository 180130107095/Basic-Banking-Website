from django.db import models


class User(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 40)
    age = models.IntegerField(null=False)
    current_credit = models.IntegerField()

    def __str__(self):
        return self.name+ ' | Credit: ' +str(self.current_credit)

# Create your models here.
