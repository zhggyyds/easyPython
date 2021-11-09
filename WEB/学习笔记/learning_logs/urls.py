"""定义learning_logs的URL模式"""

from django.urls import path

# . 为当前目录
from . import views

# 命名空间 用作模板中的url模式访问
app_name = 'learning_logs'
urlpatterns = [
    # 网址  需要调用的view中的函数  别名
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 显示某个主题
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # 创建主题
    path('new_topic/', views.new_topic, name='new_topic'),
    # 编辑新条目
    path('edit_topic/<int:topic_id>/', views.edit_topic, name= 'edit_topic'),
    # 删除新条目
    path('delete_entry/<int:topic_id>/', views.delete_topic, name= 'delete_topic'),
    # 创建新条目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 编辑新条目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name= 'edit_entry'),
    # 删除新条目
    path('delete_entry/<int:entry_id>/', views.delete_entry, name= 'delete_entry'),
]