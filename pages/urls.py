from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('global_post',views.global_post,name='global_post'),
    path('update_post/<int:id>',views.update_post,name='update_post'),
    path('create_post/',views.create_post,name='create_post'),
    path('all_post/',views.all_post,name='all_post'),
    path('search_post/',views.search_post,name='search_post'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post'),
]