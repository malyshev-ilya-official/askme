from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hot/', views.HotView.as_view(), name='hot'),
    path('question/<int:id>/', views.QuestionView.as_view(), name='question'),
    path('ask/', views.AskView.as_view(), name='ask'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('tag/<slug:slug>', views.TagView.as_view(), name='tag'),
]