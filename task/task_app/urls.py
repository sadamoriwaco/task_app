from django.urls import path
from .import views
from .views import TaskList,TaskDetail,TaskCreate,TaskDelete,TaskUpdate


app_name = 'task_app'
urlpatterns = [
    # path('', views.index,name='index'),
    path('list/', TaskList.as_view(),name= 'list'),
    path('detail/', TaskDetail.as_view(),name= 'detail'),
    path('create/', TaskCreate.as_view(),name= 'create'),
    path('delete/<int:pk>', TaskDelete.as_view(),name= 'delete'),
    path('update/<int:pk>', TaskUpdate.as_view(),name= 'update'),    
]
