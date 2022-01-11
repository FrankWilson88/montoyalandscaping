from django.db import models

# Create your models here.

class About(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/about/')
    mission = models.TextField()
    fbLink = models.CharField(max_length=200, null=True, blank=True, default='https://www.facebook.com/Montoya-Landscaping-Services-856645058033759')
    phone = models.CharField(max_length=15, null=True, blank=True, default='(443) 605-4933')
    email = models.EmailField(max_length=100, null=True, blank=True, default='Montoya18296@gmail.com')
    ownerComment = models.TextField()
    crewComment = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'About'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.mission} | {self.fbLink} {self.phone} {self.email}'

class Mulch(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/mulch/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Mulching'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'

class Trimming(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/trimming/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Trimming'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'

class Mowing(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/mowing/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Mowing'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'

class Tree(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/tree/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Tree Removal'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'


class Stone(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/stone/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Stone Install'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'

class Powerwash(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/powerwash/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Power Washing'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'

class Hardscape(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/hardscape/')
    description = models.TextField()
    class Meta:
        ordering = ['timestamp']
        verbose_name_plural = 'Hardscape'
    def __str__(self):
        return f'{self.timestamp} | {self.image} | {self.description}'
