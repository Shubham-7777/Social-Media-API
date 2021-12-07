#############################
#normal django start
#########################
"""
from django import forms
from .models import Post, Like, Comment, Profile



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile 
        fields= '__all__'
        # fields = ['username', 'country', 'dob', 'contact.phone_no', 'contact.e_mail','profile_image']




class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post 
        fields= ['username', 'slug', 'post_image', 'post_text']
        # fields= '__all__'
        # exclude = 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

#############################
#normal django end
#########################
"""`