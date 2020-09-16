from django.urls import path
from . import views
urlpatterns =[
    path('',views.PostList.as_view(),name='index'),
    path(r'^(?P<pk>\d+)/$',views.post_detail,name='post_detail')
]