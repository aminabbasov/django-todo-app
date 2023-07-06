from django.urls import path

from .views import *


urlpatterns = [
    path('register/', ReminderRegisterView.as_view(), name='register-page'),
    path('login/', ReminderLoginView.as_view(), name='login-page'),
    path('logout/', ReminderLogoutView.as_view(), name='logout-action'),

    path('', ReminderListView.as_view(), name='list-page'),
    path('archive/', ReminderArchiveListView.as_view(), name='archive-page'),
    path('search/', ReminderSearchListView.as_view(), name='search-page'),

    path('archive/<int:pk>/', reminder_archive_view, name='archive-action'),
    path('unarchive/<int:pk>/', reminder_unarchive_view, name='unarchive-action'),

    path('create/', ReminderCreateView.as_view(), name='create-page'),
    path('update/<int:pk>/', ReminderUpdateView.as_view(), name='update-page'),
    path('delete/<int:pk>/', ReminderDeleteView.as_view(), name='delete-page'),
]
