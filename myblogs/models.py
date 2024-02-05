from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Blog_Category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='images/')
    # blogcat_description=models.CharField(max_length=100)
    blogcat_description=RichTextField(blank=True)
    def __str__(self):
        return self.blog_cat
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200)
    def __str__(self):
        return self.u_email
    
class Subscription(models.Model):
    u_email = models.EmailField()
    def __str__(self):
        return self.u_email
    
class blog_post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField(blank=True)
    blog_cat=models.ForeignKey(Blog_Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_name

