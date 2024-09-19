from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomerUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Doctor(models.Model):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=255)
    availability = models.TextField(blank=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"
    

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ['doctor', 'date', 'start_time', 'end_time']

    def __str__(self):
        return f"{self.doctor} - {self.date} {self.start_time}-{self.end_time}"
    
class Booking(models.Model):
    name = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    services = models.CharField(max_length=255, blank=True)
    doctor = models.CharField(max_length=255, blank=True)
    date = models.DateField(max_length=15, blank=True)
    time = models.TimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.services}"

    