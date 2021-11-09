from django.shortcuts import render,redirect

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空表单
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            # 将数据存储进数据库并返回新建的用户对象
            new_user = form.save()
            # 使用新建用户信息自动登入
            login(request,new_user)
            # 重定向回主页
            return redirect('learning_logs:index')
    
    context = {'form':form}
    return render(request,'registration/register.html', context)