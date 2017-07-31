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
        blank=False, null=True
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
    value = models.IntegerField(null=True, blank = False)
    imun_value = models.CharField(max_length=30, null=True, blank = True)
    status = models.CharField(max_length=20, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return str(self.baby.id_baby)

    def update_status(self):
        if self.baby.jenis_kelamin == 'Laki-laki':
            if self.check == 'height':
                if self.baby.umur_bulan_bayi() == 36 or self.baby.umur_bulan_bayi() == 35 or self.baby.umur_bulan_bayi() == 34:
                    if self.value == 105:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 33 or self.baby.umur_bulan_bayi() == 32 or self.baby.umur_bulan_bayi() == 31:
                    if self.value == 100:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 30 or self.baby.umur_bulan_bayi() == 29 or self.baby.umur_bulan_bayi() == 28:
                    if self.value == 95:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 27 or self.baby.umur_bulan_bayi() == 26 or self.baby.umur_bulan_bayi() == 25:
                    if self.value == 90:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 24 or self.baby.umur_bulan_bayi() == 23 or self.baby.umur_bulan_bayi() == 22:
                    if self.value == 85:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 21 or self.baby.umur_bulan_bayi() == 20 or self.baby.umur_bulan_bayi() == 19:
                    if self.value == 80:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 18 or self.baby.umur_bulan_bayi() == 17 or self.baby.umur_bulan_bayi() == 16:
                    if self.value == 75:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 15 or self.baby.umur_bulan_bayi() == 14 or self.baby.umur_bulan_bayi() == 13:
                    if self.value == 70:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 12 or self.baby.umur_bulan_bayi() == 11 or self.baby.umur_bulan_bayi() == 10:
                    if self.value == 65:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 9 or self.baby.umur_bulan_bayi() == 8 or self.baby.umur_bulan_bayi() == 7:
                    if self.value == 60:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 6 or self.baby.umur_bulan_bayi() == 5 or self.baby.umur_bulan_bayi() == 4:
                    if self.value == 55:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'      
                if self.baby.umur_bulan_bayi() == 3 or self.baby.umur_bulan_bayi() == 2 or self.baby.umur_bulan_bayi() == 1:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'  
                

            if self.check == 'weight':
                if self.baby.umur_bulan_bayi() == 36 or self.baby.umur_bulan_bayi() == 35 or self.baby.umur_bulan_bayi() == 34:
                    if self.value == 17:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 33 or self.baby.umur_bulan_bayi() == 32 or self.baby.umur_bulan_bayi() == 31:
                    if self.value == 16:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 30 or self.baby.umur_bulan_bayi() == 29 or self.baby.umur_bulan_bayi() == 28:
                    if self.value == 14:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 27 or self.baby.umur_bulan_bayi() == 26 or self.baby.umur_bulan_bayi() == 25:
                    if self.value == 13:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 24 or self.baby.umur_bulan_bayi() == 23 or self.baby.umur_bulan_bayi() == 22:
                    if self.value == 12:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 21 or self.baby.umur_bulan_bayi() == 20 or self.baby.umur_bulan_bayi() == 19:
                    if self.value == 11:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 18 or self.baby.umur_bulan_bayi() == 17 or self.baby.umur_bulan_bayi() == 16:
                    if self.value == 10:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 15 or self.baby.umur_bulan_bayi() == 14 or self.baby.umur_bulan_bayi() == 13:
                    if self.value == 9:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 12 or self.baby.umur_bulan_bayi() == 11 or self.baby.umur_bulan_bayi() == 10:
                    if self.value == 7:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 9 or self.baby.umur_bulan_bayi() == 8 or self.baby.umur_bulan_bayi() == 7:
                    if self.value == 6:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 6 or self.baby.umur_bulan_bayi() == 5 or self.baby.umur_bulan_bayi() == 4:
                    if self.value == 5:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'      
                if self.baby.umur_bulan_bayi() == 3 or self.baby.umur_bulan_bayi() == 2 or self.baby.umur_bulan_bayi() == 1:
                    if self.value == 3:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                

            if self.check == 'headcircumference':
                if self.baby.umur_bulan_bayi() == 36 or self.baby.umur_bulan_bayi() == 35 or self.baby.umur_bulan_bayi() == 34:
                    if self.value == 51:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 33 or self.baby.umur_bulan_bayi() == 32 or self.baby.umur_bulan_bayi() == 31:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 30 or self.baby.umur_bulan_bayi() == 29 or self.baby.umur_bulan_bayi() == 28:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 27 or self.baby.umur_bulan_bayi() == 26 or self.baby.umur_bulan_bayi() == 25:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 24 or self.baby.umur_bulan_bayi() == 23 or self.baby.umur_bulan_bayi() == 22:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 21 or self.baby.umur_bulan_bayi() == 20 or self.baby.umur_bulan_bayi() == 19:
                    if self.value == 49:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 18 or self.baby.umur_bulan_bayi() == 17 or self.baby.umur_bulan_bayi() == 16:
                    if self.value == 49:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 15 or self.baby.umur_bulan_bayi() == 14 or self.baby.umur_bulan_bayi() == 13:
                    if self.value == 48:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 12 or self.baby.umur_bulan_bayi() == 11 or self.baby.umur_bulan_bayi() == 10:
                    if self.value == 47:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 9 or self.baby.umur_bulan_bayi() == 8 or self.baby.umur_bulan_bayi() == 7:
                    if self.value == 46:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 6 or self.baby.umur_bulan_bayi() == 5 or self.baby.umur_bulan_bayi() == 4:
                    if self.value == 44:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'      
                if self.baby.umur_bulan_bayi() == 3 or self.baby.umur_bulan_bayi() == 2 or self.baby.umur_bulan_bayi() == 1:
                    if self.value == 41:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                
        if self.baby.jenis_kelamin == 'Perempuan':
            if self.check == 'height':
                if self.baby.umur_bulan_bayi() == 36 or self.baby.umur_bulan_bayi() == 35 or self.baby.umur_bulan_bayi() == 34:
                    if self.value == 105:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 33 or self.baby.umur_bulan_bayi() == 32 or self.baby.umur_bulan_bayi() == 31:
                    if self.value == 100:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 30 or self.baby.umur_bulan_bayi() == 29 or self.baby.umur_bulan_bayi() == 28:
                    if self.value == 95:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 27 or self.baby.umur_bulan_bayi() == 26 or self.baby.umur_bulan_bayi() == 25:
                    if self.value == 90:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 24 or self.baby.umur_bulan_bayi() == 23 or self.baby.umur_bulan_bayi() == 22:
                    if self.value == 85:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 21 or self.baby.umur_bulan_bayi() == 20 or self.baby.umur_bulan_bayi() == 19:
                    if self.value == 80:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 18 or self.baby.umur_bulan_bayi() == 17 or self.baby.umur_bulan_bayi() == 16:
                    if self.value == 75:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 15 or self.baby.umur_bulan_bayi() == 14 or self.baby.umur_bulan_bayi() == 13:
                    if self.value == 70:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 12 or self.baby.umur_bulan_bayi() == 11 or self.baby.umur_bulan_bayi() == 10:
                    if self.value == 65:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 9 or self.baby.umur_bulan_bayi() == 8 or self.baby.umur_bulan_bayi() == 7:
                    if self.value == 60:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 6 or self.baby.umur_bulan_bayi() == 5 or self.baby.umur_bulan_bayi() == 4:
                    if self.value == 55:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'      
                if self.baby.umur_bulan_bayi() == 3 or self.baby.umur_bulan_bayi() == 2 or self.baby.umur_bulan_bayi() == 1:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   

            if self.check == 'weight':
                if self.baby.umur_bulan_bayi() == 36 or self.baby.umur_bulan_bayi() == 35 or self.baby.umur_bulan_bayi() == 34:
                    if self.value == 16:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 33 or self.baby.umur_bulan_bayi() == 32 or self.baby.umur_bulan_bayi() == 31:
                    if self.value == 15:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 30 or self.baby.umur_bulan_bayi() == 29 or self.baby.umur_bulan_bayi() == 28:
                    if self.value == 14:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 27 or self.baby.umur_bulan_bayi() == 26 or self.baby.umur_bulan_bayi() == 25:
                    if self.value == 13:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 24 or self.baby.umur_bulan_bayi() == 23 or self.baby.umur_bulan_bayi() == 22:
                    if self.value == 12:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 21 or self.baby.umur_bulan_bayi() == 20 or self.baby.umur_bulan_bayi() == 19:
                    if self.value == 11:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 18 or self.baby.umur_bulan_bayi() == 17 or self.baby.umur_bulan_bayi() == 16:
                    if self.value == 10:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 15 or self.baby.umur_bulan_bayi() == 14 or self.baby.umur_bulan_bayi() == 13:
                    if self.value == 9:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 12 or self.baby.umur_bulan_bayi() == 11 or self.baby.umur_bulan_bayi() == 10:
                    if self.value == 7:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 9 or self.baby.umur_bulan_bayi() == 8 or self.baby.umur_bulan_bayi() == 7:
                    if self.value == 5:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 6 or self.baby.umur_bulan_bayi() == 5 or self.baby.umur_bulan_bayi() == 4:
                    if self.value == 4:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'      
                if self.baby.umur_bulan_bayi() == 3 or self.baby.umur_bulan_bayi() == 2 or self.baby.umur_bulan_bayi() == 1:
                    if self.value == 3:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
               

            if self.check == 'headcircumference':
                if self.baby.umur_bulan_bayi() == 36 or self.baby.umur_bulan_bayi() == 35 or self.baby.umur_bulan_bayi() == 34:
                    if self.value == 50:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 33 or self.baby.umur_bulan_bayi() == 32 or self.baby.umur_bulan_bayi() == 31:
                    if self.value == 49:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 30 or self.baby.umur_bulan_bayi() == 29 or self.baby.umur_bulan_bayi() == 28:
                    if self.value == 49:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 27 or self.baby.umur_bulan_bayi() == 26 or self.baby.umur_bulan_bayi() == 25:
                    if self.value == 49:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 24 or self.baby.umur_bulan_bayi() == 23 or self.baby.umur_bulan_bayi() == 22:
                    if self.value == 48:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 21 or self.baby.umur_bulan_bayi() == 20 or self.baby.umur_bulan_bayi() == 19:
                    if self.value == 47:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 18 or self.baby.umur_bulan_bayi() == 17 or self.baby.umur_bulan_bayi() == 16:
                    if self.value == 47:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 15 or self.baby.umur_bulan_bayi() == 14 or self.baby.umur_bulan_bayi() == 13:
                    if self.value == 47:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                if self.baby.umur_bulan_bayi() == 12 or self.baby.umur_bulan_bayi() == 11 or self.baby.umur_bulan_bayi() == 10:
                    if self.value == 46:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 9 or self.baby.umur_bulan_bayi() == 8 or self.baby.umur_bulan_bayi() == 7:
                    if self.value == 45:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'   
                if self.baby.umur_bulan_bayi() == 6 or self.baby.umur_bulan_bayi() == 5 or self.baby.umur_bulan_bayi() == 4:
                    if self.value == 43:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'      
                if self.baby.umur_bulan_bayi() == 3 or self.baby.umur_bulan_bayi() == 2 or self.baby.umur_bulan_bayi() == 1:
                    if self.value == 40:
                        self.status = 'ideal'
                    else:
                        self.status ='tidak ideal'
                
              
class Event (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)
    date_event = models.DateField(
        blank = False, null=True)
        

    def __str__(self):
        return self.title

# Create your models here.

