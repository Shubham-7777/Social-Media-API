from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import test, ProfileAPIView, CreateProfileAPIView, PostAPIView, CreatePostAPIView
from django.contrib.auth.decorators import login_required, permission_required



app_name = 'profiles_app'


urlpatterns = [
    path('', test, name="test_url"),
    path("profile/<slug:username>/", ProfileAPIView.as_view(), name="profile_url"),
    path("create-profile/", login_required(CreateProfileAPIView.as_view()), name="create_profile_url"),


    path("create-post/", CreatePostAPIView.as_view(), name="create_post_url"),
    path("posts/<int:id>/", PostAPIView.as_view(), name="post_url")


]























##################################################

#DRF API start
#################################################
"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
from .views import ProfileViewSet, PostViewSet, FriendsViewSet

router = DefaultRouter()

router.register('profiles', ProfileViewSet)
router.register('posts', PostViewSet)
router.register('friends', FriendsViewSet)


urlpatterns = router.urls

urlpatterns = [

    path('posts/', PostView.as_view(), name='post_url')

]


#path('profile/', ProfileView.as_view(), name='profile_url'),
#path('<int:pk>/', ProfileView.as_view(),name='profile_change'),
   
##################################################

#DRF API end
#################################################



    
"""
###########################

#normal django start
############################
"""
from django.urls import include, path, re_path
from django.conf import settings
from . import views 

app_name = 'user_profile_app'

urlpatterns = [
    path('test/', views.test_view, name="test"),
    path("friends/", views.friends_view, name="friends_url"),
    path('', views.home_page_view, name='home_page_url'),
    path("profile_create/", views.profile_create_view, name='profile_create_url'),
    path("profile_detail/", views.profile_detail_view, name='profile_detail_url'),
    path("post_create/", views.post_create_view, name='post_create_url'),
    path("<slug:my_slug>/details/", views.post_detail_view, name='post_detail_url'),
    #path("<slug:username>/send_request/", views.send_request, name='send-request'),
    path("<slug:username>/reject/", views.reject_view, name="reject_url"),
    
    # (r'^user/(?P<username>\w{0,50})/$'
    # path('index/', views.test_view, name='index_page_url'),
    # path('test/', views.test_view, name="test_url"),
    # path("search/results/", views.search_view, name='search_url'),

] 


if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

###########################

#normal django end
############################
"""