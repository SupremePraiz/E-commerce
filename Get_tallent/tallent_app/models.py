from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Contractor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contractor_images/')
    about = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])  # Example regex for phone number validation
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='employer_images/')
    about = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])  # Example regex for phone number validation
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class JobPost(models.Model):
    post = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='comments')
    review = models.TextField(max_length=500)  # Adjust max_length as needed
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
