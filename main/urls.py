from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('home/announcements/<str:pk>',views.announce,name = "announce"),
    path('calendar/',views.calendar, name="calendar"),
    path('courseSelect/',views.courseSelect, name="courseSelect"),
    path('courseHome/<str:pk>',views.courseHome,name="courseHome"),
    path('courseHome/<str:pk1>/assignmentSubmit/<str:pk2>/',views.assignmentSub,name="AssignmentSub"),
    path('room/<str:pk>',views.room,name="room")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   