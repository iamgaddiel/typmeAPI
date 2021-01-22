from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Condition(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    MEDICATION_FORM = [
        ("Pills", "Pills"),
        ("Powder", "Powder"),
    ]

    DOSAGE_LIST = [
        ("mg", "mg"),
        ("mcg", "mcg"),
        ("g", "g"),
    ]

    DRUG_FREQUENCY = [
        ("6HRS", "6HRS"),
        ("8HRS", "8HRS"),
        ("12HRS", "12HRS"),
        ("24HRS", "24HRS"),
    ]

    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    form = models.CharField(max_length=25, help_text="What form is your medication")
    dosage = models.CharField(max_length=3)
    amount = models.PositiveIntegerField(help_text="amount of medications to be taken")
    frequency = models.TimeField(null=True)
    condition = models.CharField(max_length=50)

    # name = models.CharField(max_length=100)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # form = models.CharField(max_length=25, choices=MEDICATION_FORM, help_text="What form is your medication")
    # dosage = models.CharField(max_length=3, choices=DOSAGE_LIST)
    # amount = models.PositiveIntegerField(help_text="amount of medications to be taken")
    # frequency = models.TimeField(null=True)
    # condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name="condition")

    def __str__(self):
        return f"{self.user} => {self.name} | {self.frequency}"
