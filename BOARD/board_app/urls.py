from django.contrib import admin
from django.urls import path, include
from .views import PostsList, AddList, PostEdit, PostDelete, PostDetail, ResponseAdd, ResponseList, ResponseDelete

urlpatterns = [
    path('', PostsList.as_view()),
    path('add/', AddList.as_view(), name='post_add'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('response_add/', ResponseAdd.as_view(), name='response_add'),
    path('response_list/', ResponseList.as_view()),
    path('response_list/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete')
]