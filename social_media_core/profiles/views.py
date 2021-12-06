
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer
from rest_framework import viewsets, status, filters
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
class ProfileAPIView(APIView):
    
    def get(self, request, username):
        print(username)
        obj = Profile.objects.filter(username__username=username)
        print(obj)
        if obj.exists():
            serializer = ProfileSerializer(obj, many=True) 
            return Response({"message": "User avaliable",
                            "Data" : serializer.data}, 
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "User does not exist"},
                            status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, username):
        obj = Profile.objects.filter(username=username)
        if obj.exists():
            obj.delete()
            return Response("Successfully Deleted", 
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "User does not exist"}, 
                            status=status.HTTP_404_NOT_FOUND)



class CreateProfileAPIView(APIView):
    
    def post(self, request):
        print(request.data)
        profile_picture = request.data.get('profile_picture')
        check_user = Profile.objects.filter(username=request.data.get('username'))
        if check_user:
            return Response({"message" : "user already exist, plz choose another username"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                print("Error in Serializer")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostAPIView(APIView):
    
    def get(self, request, id):
        post_obj = Post.objects.filter(id=id)
        if post_obj:        
            serializer = PostSerializer(post_obj, many=True)        
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, id):
        post_obj = get_object_or_404(Post, id=id)
        if post_obj:
            post_obj.delete()
            return Response({"message":"Post Deleted Successfully"},  status=status.HTTP_200_OK)
        else:
            return Response({"message" : "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
        


class CreatePostAPIView(APIView):

    #@method_decorator(login_required())
    def post(self, request):
        print(request.data, "request.data")
        #user = Profile.objects.filter(username__username = request.user).first()
        serializer = PostSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("Error in Serializer")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
































def test(request):
    a = "Testing"
    context = {
        "a" : a
    }
    template_name = "test.html"
    return render(request, template_name, context)





##################################################

#DRF API start
#################################################
"""
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import mixins, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action

from .models import Profile, Post, Friend, Like, Comment
from .permissions import IsAdminProfileOrReadOnly, IsAdminPostOrReadOnly
from .serializers import ProfileSerializer, PostSerializer, FriendSerializer, CommentSerializer, LikeSerializer
# Create your views here.
"""
# Profile
"""
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,IsAdminProfileOrReadOnly]



    def create(self, request, *args, **kwargs):
        user = request.user.id
        obj = User.objects.get(id=request.user.id)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        bio = request.data.get('bio')
        location = request.data.get('location')
        profile_picture = request.data.get('profile_picture')
        data = Profile.objects.create(user=obj, first_name=first_name,last_name=last_name, bio=bio, location=location ,profile_picture=profile_picture)
        data.save()
        return JsonResponse({"response": "added successful"})

"""





"""
def create(self, request, *args, **kwargs):
    uid = request.user.id
    username = request.user.username
    print(uid, username)
    user.save()
user = User.objects.get(id=uid)
user.first_name = request.date.get('first_name')
user.last_name = request.date.get('last_name')
user.bio = request.date.get('bio')
user.location = request.date.get('location')
user.profile_picture = request.date.get('profile_picture')


def list(self, request, *args, **kwargs):
    user = User.objects.get(id=request.user.id)
"""
        

"""
    def update(self, request, *args, **kwargs):
        try:
            qs = Profile.objects.get(user__username = self.request.user)
            if qs.exists():
                serializer = self.serializer_class(qs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
"""
"""

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminPostOrReadOnly]
    #parser_classes = (MultiPartParser, FormParser, JSONParser)


    def update(self, request, *args, **kwargs):
        try:
            user_id = kwargs.get('pk')
            print(user_id)            
            qs = self.queryset.filter(id=user_id)
            if qs.exists:
                serializer = self.serializer_class(qs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated, IsAdminPostOrReadOnly]


    
    def list(self, request, *args, **kwargs):
        a = request.user
        print(a)
        friends = Friend.objects.filter(username__user__username = a).values_list('friend_id', flat=True)
        print(friends)
        data = [Profile.objects.get(id = i) for i in friends]
        serializer = ProfileSerializer(data, many=True)
        print(data)
        print(serializer.data)
        print('Friends list')
        return Response(serializer.data, status=status.HTTP_200_OK)
            

"""
"""
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')  
        print(user_id) 
        user = Friend.objects.filter(id = user_id)
        print(user)
        if user.exists():
            friends_list = [Profile.objects.get(id = friend.username.user.id) for friend in user]
            print(friends_list)
            serializer = self.serializer_class(qs, many=True)
            serializer = ProfileSerializer(friends_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

"""






"""
class PostView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'backend/home.html'
    serializer_class = PostSerializer


    def get(self, request, format=None):
        post_list = Post.objects.filter(username__user__username = request.user)
        
        return Response({'post_obj' : post_list}, status=status.HTTP_201_CREATED)
"""

"""
class ProfileView(generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,] 


    def get(self, request, format=None):
        obj = Profile.objects.filter(user__username = request.user)
        serializer = ProfileSerializer(obj, many=True)
        return Response(serializer.data)


def patch(self, request):
    profile = Profile.objects.filter(user = request.user).first()
    print(profile)
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
"""
##################################################

#DRF API end
#################################################





##############################################
# normal django start
##############################################


"""


# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.auth import authenticate, login
from django.utils import timezone 
from .forms import LoginForm, PostForm, ProfileForm, CommentForm
from .models import Post, Like, Comment, Profile, Friends
# Create your views here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages


User = settings.AUTH_USER_MODEL


def test_view(request):
    a = Friends.objects.all()
    template_name = 'test.html'
    context = {
        "a" : a
        }
    return render(request, template_name, context)


def home_page_view(request):
    #obj_post = Post.objects.filter(username__username=request.user)
    #obj_profile = Profile.objects.filter(post__username__username=request.user)
    a = request.POST.get("comment", None)
    if request.user.is_authenticated:
        obj = Post.objects.filter(username__username=request.user)
        #obj = Friends.objects.all()[::-1]
        obj_profile = Profile.objects.filter(username=request.user)

    else:
        obj = Post.objects.all()

    template_name = 'user_profile_app/feed.html'

    context = {
        "obj" : obj,
        "obj_profile" : obj_profile
        #'obj_profile' : obj_profile,
    }
    return render(request, template_name, context)
    

def profile_create_view(request):
    if request.method =="POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            print("Valid")
            form.save()
        template_name = 'user_profile_app/profile_create.html'
        context = {
            'form' : form
            }
        return render(request, template_name, context)
    else:
        form = LoginForm()
    template_name = 'user_profile_app/profile_create.html'
    context = {
        'form' : form
        }
    return render(request, template_name, context)    


def profile_detail_view(request):
    obj = Profile.objects.filter(username=request.user)
    template_name = 'user_profile_app/profile_details.html'
    context = {
        "obj" : obj
        }
    return render(request, template_name, context)



def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES )
        if form.is_valid():
            
            obj = form.save(commit=False)
            obj.username = form.cleaned_data.get('username')
            # obj.contact = form.cleaned_data.get('contact')
            obj.post_image = form.cleaned_data.get('post_image')
            obj.post_text = form.cleaned_data.get('post_text')
            obj.slug = form.cleaned_data.get('slug')
            obj.save()
            print("Valid")
            form.save()
        template_name = 'user_profile_app/post_create.html'
        context = {
            'form' : form
            }
        return render(request, template_name, context)
    else:
        print("Invalid")
        form = PostForm()
    template_name = 'user_profile_app/post_create.html'
    context = {
        'form' : form
        }
    return render(request, template_name, context)  



def post_detail_view(request, my_slug):
    #obj = get_list_or_404(Post, slug=my_slug)
    a = request.POST.get("comment")
    obj = Post.objects.filter(slug=my_slug)
    obj_profile = Profile.objects.get(username=request.user)
    print(a, obj, obj_profile)
    b = Comment(comment_text=a, image=obj[0], comment=obj_profile)
    b.save()
    template_name = 'user_profile_app/post_detail.html'
    obj_comment = Comment.objects.filter(image__slug=my_slug)
    context = {
        "obj": obj,
        "obj_comment" : obj_comment
        }
    return render(request, template_name, context)



def send_request(request, username):
    if username is not None:
        current_user = Profile.objects.get(username = request.user)
        friend_user = Profile.objects.get(username__username = username)
        a = Friends.objects.filter(friend__username__username = username)
        if a.exists():
            messages.info(request,"User is already your Friend!!")
            response = redirect('/friends/')
            return response
        else:
            messages.info(request, "User added to your Friends List !!")
            
            obj = Friends.objects.create(user = current_user, friend = friend_user)
            obj.save()
            response = redirect('/friends/')
            return response
    else:   
        pass    


def reject_view(request, username):
    if username is not None:
        obj = Friends.objects.filter(friend__username__username=username)
        print(obj)
        if obj.exists():
            messages.info(request, "User deleted from your Friends List !!")
            obj.delete()
            response = redirect('/friends/')
            return response
        else:
            messages.info(request, "Already not your Friend!!")
            response = redirect('/friends/')
            return response
    else:
        pass         
    



def friends_view(request):
    a = request.GET.get('Reject', None)
    print(a, 'reject')
    friend = Friends.objects.all()[::-1]
    print(friend, 'Friends')
    find_friend = Profile.objects.exclude(username__username = friend).exclude(username = request.user)


    print(find_friend, 'Profile')
    template_name = 'user_profile_app/friends.html'
    context = {
        'friend' : friend,
        'find_friend' : find_friend
        
    }
    return render(request, template_name, context)

"""



"""
def post_update_view(request, my_slug):
    data = get_object_or_404(Post, slug=my_slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        obj = form.save(commit=False)
        form.save()
    template_name = 'user_profile_app/post_update.html'
    context = {
        'obj_data' : data,
        'form': form
        }
    return render(request, template_name, context)



@staff_member_required()
def post_delete_view(request, my_slug):
    obj = get_object_or_404(Post, slug=my_slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/home")
    template_name = "user_profile_app/post_delete.html"
    context = {"obj_delete": obj
               }
    return render(request, template_name, context)


@login_required
def search_view(request):
    print(request.user)
    query = request.GET.get('q', None)
    #obj = Post.objects.filter(slug__icontains=query)
    obj = Post.objects.filter(username__username__username__icontains=query)
    template_name = 'user_profile_app/search.html'
    context = {
        'obj' : obj
    }
    return render(request, template_name, context)
"""
##############################################
# normal django end
##############################################
