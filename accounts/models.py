from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# email , password, username  , first_name , last_name
class CustomUser(AbstractUser):
    class Type(models.TextChoices):
        STUDENT = "student" , "Student"
        TEACHER = "teacher" , "Teacher"

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, choices=Type.choices, default=Type.STUDENT , null=True , blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
