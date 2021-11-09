from django.shortcuts import render, redirect, get_object_or_404

from .models import Topic,Entry

from .forms import TopicForm,EntryForm

from django.contrib.auth.decorators import login_required

from django.http import Http404

def check_topic_owner(topic, request):
    """用于避免当手工输入网址访问别的用户数据的情况"""
    if topic.owner != request.user:
        raise Http404

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

#@login_required
def topics(request):
    """展示所有主题"""
    # request下包含着user信息
    if request.user.is_authenticated:
        topics = Topic.objects.filter(owner= request.user).order_by('date_added')
    else:
        topics = list(Topic.objects.all())
        for topic in topics[:]:
            if topic.public == False:
                topics.remove(topic)
                
    context = {"topics": topics}
    # context中的键是将在传入页面中使用的名称，值是数据
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """前往某主题"""
    topic = get_object_or_404(Topic, id=topic_id) # 当访问不存在页面时会显示404错误页面而不是500
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """新建主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        # 检查表达有效性
        if form.is_valid():
            # 在数据库中保存表单
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            # 导向回topics的视图函数进行数据处理
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def edit_topic(request,topic_id):
    """编辑主题"""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求,使用当前topic填充表单(修改topic先显示原始数据给用户)
        form = TopicForm(instance=topic)
    else:
        # POST提交数据，对数据进行处理
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form, 'topic':topic}
    # 无效后或者初次请求转向的显示网址
    return render(request, 'learning_logs/edit_topic.html', context)

@login_required
def delete_topic(request,topic_id):
    """删除主题"""
    # 删除相应条目
    Topic.objects.filter(id = topic_id).delete()

    return redirect('learning_logs:topics')

@login_required
def new_entry(request,topic_id):
    """新建条目"""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            #先不提交至数据库
            new_entry = form.save(commit=False)
            # 此处将entry与topic关联
            new_entry.topic = topic
            #关联后再保存
            new_entry.save()
            # 回到相关主题的views函数进行数据处理
            return redirect('learning_logs:topic',topic_id=topic_id)

    # 用于用户刚进入页面或提交表单数据无效时执行
    context = {'topic': topic,'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    """编辑条目"""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求使用当前entry填充表单(修改entry先显示原始数据给用户)
        form = EntryForm(instance=entry)
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic,'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def delete_entry(request,entry_id):
    """删除条目，并返回相关topic网页"""
    entry = Entry.objects.get(id=entry_id)
    # 删除相应条目
    Entry.objects.filter(id = entry_id).delete()
    topic = entry.topic

    return redirect('learning_logs:topic', topic_id=topic.id)

