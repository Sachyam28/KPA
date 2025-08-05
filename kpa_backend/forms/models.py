from django.db import models

# Create your models here.

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()

    def __str__(self):
        return self.formNumber


class BogieChecksheet(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bogieDetails = models.JSONField()
    bogieChecksheet = models.JSONField()
    bmbcChecksheet = models.JSONField()

    def __str__(self):
        return self.formNumber