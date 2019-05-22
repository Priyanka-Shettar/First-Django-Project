from django.urls import path,include
from webpage import views
from django.conf.urls import url



urlpatterns = [
    #path('', views.HomePageView.as_view()),
    # app_name='webpage'
    path('', views.Home.as_view(),),
    url(r'about/', views.About.as_view(),name="about"),
    path(r'gallery/', views.Gallery.as_view(),name="gallery"),
    path(r'contact/', views.Contact.as_view(),name="contact"),


]
