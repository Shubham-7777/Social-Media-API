from django.db import models
from django.contrib.auth.models import User
#from django_currentuser.middleware import get_current_authenticated_user
from django_currentuser.db.models import CurrentUserField


class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile-pictures', null=True, blank=True)


    def __str__(self):
        return str(self.username)

    
    def get_username(self):
        return self.username

"""    
    def get_username_id(self):
        return self.uername.id
    
    def get_profile_id(self):
        return self.id
    
    def get_first_name(self):
        return self.first_name
"""



class Post(models.Model):
    #posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posted_by')
    #########################
    # For TEMPORARY I added  Currrect FIeld to work but need to add FOREIGN KEY in posted_by
    ######################### 
    posted_by = CurrentUserField(related_name='posted_by')
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='post-images', null=True)
    #pub_date = models.DateTimeField('Publication Date',auto_now=True, auto_now_add=False)


    def get_readable_date(self):
        return self.pub_date.strftime("%B %d, %Y")

"""
    def __str__(self):
        return f'{self.posted_by.username} {self.text}'

    def get_post_id(self):
        return self.id
    """
"""
    def get_profile_id(self):
        return self.username.id
"""
"""
    def get_username(self):
        return self.username.user.username
"""
"""
class Friends(models.Model):
    username = models.ForeignKey(Profile, related_name='username', on_delete=models.CASCADE)
    friend = models.ForeignKey(Profile, related_name='friend',on_delete=models.CASCADE) 

    def __str__(self):
        return f"Friendship {self.username.user .username} - {self.friend.user.username}"
    

    def get_sender_username(self):
        return self.username.user.username


    def get_friend_username(self):
        return self.friend.user.username

"""

class Like(models.Model):
    like = models.BooleanField(null=True, blank=True, default=False)
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by =  models.ForeignKey(Profile, on_delete=models.CASCADE)    


    def __str__(self):
        return str(self.liked_by) + str(self.liked_post)
     

class Comment(models.Model):
    comment = models.TextField(max_length=500)
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_by =  models.ForeignKey(Profile, on_delete=models.CASCADE)    


    def __str__(self):
        return str(self.commented_by) + str(self.commented_post)















#############################
# DRF API start
########################
"""







"""
#############################
# DRF API end
########################


#####################################
# normal django start
###################################
"""

# -*- coding: utf-8 -*-
# from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from django_countries.fields import CountryField
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse  

# Create your models here.

User = settings.AUTH_USER_MODEL


STATUS_CHOICES = [
    ('ON', 'ONLINE'),
    ('AW', 'AWAY'),
    ('BS', 'BUSY'),
    ('NA', 'NOT AVALIABLE'),
    ('CS', 'CUSTOM STATUS')]
        



class Profile(models.Model):
    #username = models.OneToOneField(User)
    #contact = models.OneToOneField(Contact_Info, on_delete=models.CASCADE)    
    #username = models.CharField(unique=True, blank=False, null=False, max_length=100)    
    username = models.OneToOneField(User, on_delete=models.CASCADE)    
    slug = models.SlugField(unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    e_mail = models.EmailField(max_length=254, unique=True)
    country = CountryField(blank_label="(Select Country)")
    dob = models.DateField(verbose_name="Date Of Birth")
    profile_image = models.ImageField(upload_to="image/", null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.username.username

class Post(models.Model):
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    post_image = models.ImageField(upload_to='image/')
    post_text = models.TextField(max_length=1000, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-posted_at']
    
    def __str__(self):
        return str(self.slug)

    def get_absolute_url(self):
        return f"{self.slug}"

    def get_update_url(self):
        return f"{self.slug}/update/"

    def get_delete_url(self):
        return f"{self.slug}/delete/"


class Like(models.Model):
    image = models.OneToOneField(Post, on_delete=models.CASCADE)
    like_image = models.BooleanField(null=True, default=False)


class Comment(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE)     
    comment = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=100, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.comment_text)

    #text = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    #comment_text = models.TextField(max_length=100, default="Enter your Comment")


class Friends(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user")    
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friend")
    status = models.CharField(max_length=20, default='request_sent')
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return str(self.friend.username.username)

#####################################
# normal django end
###################################
"""