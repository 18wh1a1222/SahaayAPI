from django.urls import path

from . import views

urlpatterns = [
    path('aadhar/', views.AadharApi, name="aadharDetails"),
    path('eventDetails/', views.EventDetailsApi, name="eventDetails"),
    path('login', views.LoginApi, name="login"),
    path('sahaay/', views.UserApi, name='allUsers'),
    path('sahaay/<str:phno>/', views.UserApi, name='user'),
    path('needs/', views.NeedsApi, name='allNeeds'),
    path('events/', views.EventsApi, name="events"),
    path('needs/<str:status>/', views.NeedsApi, name='needs'),
    path('needs/<int:needId>/', views.NeedsApi, name='needid'),
    path('needs/<str:userId>/', views.NeedsApi, name="needsphno"),
    path('needs/<str:status>/<int:needId>/', views.NeedsApi, name='needsid')
]