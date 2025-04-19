from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class chaimenu(models.Model):
    chaimenu_options = [
        ('ML','masala chai'),
        ('SL','spiced lemon chai'),
        ('TL','tender lemon chai'),
        ('NC','normal chai'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    timedate = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chaimenu_options)
    description = models.TextField(default='')
    # price = models.IntegerField()

    def __str__(self):
        # return self.name
        # return self.type
        return f"{self.name} - {self.type} - {self.timedate}"


# one to many relationship

class chaiReviews(models.Model):
    chai = models.ForeignKey(chaimenu,on_delete=models.CASCADE,related_name = 'reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    rating_options = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    review = models.IntegerField(choices=rating_options)
    # name = models.CharField(max_length=100)
    comment = models.TextField(default='')
    date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.chai.name} - Rating: {self.review}"

# mamy to many relationship
class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField( max_length=100)
    chai_menu = models.ManyToManyField(chaimenu, related_name='stores')

    def __str__(self):
        return self.name
    

# one to one
class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaimenu, on_delete=models.CASCADE, primary_key=True,related_name='chaiCertificate')

    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.chai.name}"
    
