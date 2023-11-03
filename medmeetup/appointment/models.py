from django.db import models
from Hospital.models import Doctor
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    time_choice = (
        ['morning', "Morning"],
        ['evening', "Evening"]
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.EmailField()
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='appointments'
    )
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices = time_choice, max_length=10)
    note = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.name}-{self.doctor.name}"

