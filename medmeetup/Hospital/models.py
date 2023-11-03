from django.db import models

# Create your models here.


class Slider(models.Model):
    caption = models.CharField(max_length=150)
    SLogan = models.CharField(max_length=120)
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.caption[:20]
    
    class Meta:
        verbose_name_plural = 'slider'


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    items = models.ManyToManyField(to='item', )
    thumbnail = models.ImageField(upload_to='services/')
    cover = models.ImageField(upload_to='services/')
    # imgae1 = models.ImageField(upload_to='services/', blank= True, null= True)
    image2 = models.ImageField(upload_to='services/', blank=True ,null= True ) 

    def __str__(self):
        return self.title
    

class Item(models.Model):
    title = title = models.CharField(max_length=120)

    def __str__(self):
        return self.title
    

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='doctors/')
    details = models.TextField()
    experience = models.TextField()
    expertise = models.ManyToManyField(to='Expertize', related_name='doctors')
    # twiter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Expertize(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.question
    

class Gallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Galleries'