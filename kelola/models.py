from datetime import date, timedelta
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

    def __unicode__(self):
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

    def __unicode__(self):
        return self.title


class BabyBio (models.Model):
    jenis_kelamin_choice = (
        ('Laki-laki', 'laki-laki'),
        ('Perempuan', 'perempuan'),
    )

    id_baby = models.AutoField(primary_key=True, unique=True)
    baby_name = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=30, choices=jenis_kelamin_choice)
    date_birth = models.DateField(
        blank=True, null=True
    )
    address = models.TextField()
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    weight_birth = models.IntegerField()
    height_birth = models.IntegerField()
    headcircumference_birth = models.IntegerField()
    parent_email = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.id_baby)

    def umur_bulan_bayi(self):
        today = date.today()
        d1 = today
        d2 = self.date_birth
        return (d1.year - d2.year)*12 + d1.month - d2.month



class History (models.Model):
    check_choices = (
        ('weight', 'Weight'),
        ('height', 'Height'),
        ('headcircumference', 'HeadCircumference'),
        ('immunization', 'Immunization'),
    )

    baby = models.ForeignKey(BabyBio, related_name='histories')    
    check = models.CharField(max_length=30, choices=check_choices)
    value = models.IntegerField(null=True, blank = True)
    imun_value = models.CharField(max_length=30, null=True, blank = True)
    status = models.CharField(max_length=20, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return str(self.baby.id_baby)

    def update_status(self):
        if self.check == 'height':
            if self.baby.umur_bulan_bayi() == 24:
                if self.value == 10:
                    self.status = 'ideal'
                else:
                    self.status ='tidak ideal'
              
class Event (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)
    date_event = models.DateField(
        blank = True, null=True)
        

    def __str__(self):
        return self.title

# Create your models here.

