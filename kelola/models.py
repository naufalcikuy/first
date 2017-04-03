from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Knowledge(models.Model):
    category_choice = (
        ('Health', 'health'),
        ('Growing', 'growing'),
        ('Development', 'development'),
        ('Immunization', 'immunization'),
    )

    category = models.CharField(max_length=20, choices = category_choice)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class BabyBio (models.Model):
    id_baby = models.AutoField(primary_key=True, unique=True)
    baby_name = models.CharField(max_length=100)
    date_birth = models.DateField(
        blank=True, null=True
    )
    address = models.TextField()
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    weight_birth = models.IntegerField()
    height_birth = models.IntegerField()
    headcircumference_birth = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)



    def __str__(self):
        return self.baby_name

# Create your models here.
