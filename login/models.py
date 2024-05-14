from django.db import models
from django.contrib.auth.models import User  # Import User model
import datetime  # Import datetime module

class Crime(models.Model):
    reference = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255)
    date_reported = models.DateField(default=datetime.date.today)
    time_reported = models.TimeField(default=datetime.time.min)
    email=models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.reference}/{self.date_reported.strftime('%m/%d/%Y')}"

class Charge(models.Model):
    description = models.TextField()
    reference = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='charges')
    
    def __str__(self):
        return str(self.reference)

class Evidence(models.Model):
    description = models.TextField()
    reference = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='evidence')
        
    def __str__(self):
        return str(self.reference)

class Investigation(models.Model):
    lead_investigator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, blank=True)
    reference = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='investigations')

    def __str__(self):
        return str(self.reference)
    
class Suspect(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    apprehended = models.BooleanField(default=False)
    gender=models.TextField(blank=True)
    reference = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='suspects')

    def __str__(self):
        return str(self.reference)

class Victim(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    reference = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='victims')

    def __str__(self):
        return str(self.reference)

class Witness(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=50, blank=True)
    reference = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name='witnesses')

    def __str__(self):
        return str(self.reference)
