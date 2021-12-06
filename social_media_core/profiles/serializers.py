from django.db.models.fields import CharField
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault

from profiles.models import Profile, Post




class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'bio', 'location', 'profile_picture']



class PostSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(source="posted_by.username", read_only=True)
    #posted_by = ProfileSerializer(read_only=True)
    #posted_by = ProfileSerializer(source = "get_username")
    #posted_by = CurrentUserDefault()
    # need to add posted by (user that posted a post) into the serializer
    #posted_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    posted_by = serializers.CharField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Post
        #"posted_by"
        fields = ["posted_by", "text", "pub_date", "image"]
        read_only_fields = ["posted_by",]










































##################################################

#DRF API start
#################################################

"""
from backend.models import Post, Profile, Friend, Like, Comment

class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.CharField(source = 'get_username')
    profile_id = serializers.IntegerField(source = 'get_profile_id')
    first_name = serializers.CharField(source = 'get_first_name')
    

    class Meta:
        model = Profile
        fields = ('user', 'profile_id', 'first_name', 'last_name', 'bio','location', 'profile_picture')
        read_only_fields = ('profile_id', 'user', )



class PostSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source = 'get_username')
    post_id = serializers.IntegerField(source = 'get_post_id')
    profile_id = serializers.IntegerField(source = 'get_profile_id')

    class Meta:
        model = Post
        fields = ('username', 'post_id','profile_id', 'text', 'pub_date', 'image')
        read_only_fields = ('username_username_username', 'username_username_id')


class FriendSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='get_sender_username')
    friend = serializers.CharField(source='get_friend_username')
    class Meta:
        model = Friend
        fields = ('username', 'friend')



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment 
        fields = ('comment', 'commented_post', 'commented_by')        



class LikeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Like
        fields = ('like', 'liked_by', 'liked_post')

##################################################

#DRF API end
#################################################
"""


