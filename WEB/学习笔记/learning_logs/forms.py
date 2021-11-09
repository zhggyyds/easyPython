from django import forms

from .models import Topic,Entry

# 表单：让用户输入并提交信息的页面都是表单

class TopicForm(forms.ModelForm):
    """主题表"""
    # Meta类会告诉django根据哪个模型创建表单，以及其中包含哪些字段
    class Meta:
        # 根据Topic模型创建表单
        model = Topic
        # fields中包含需要在表单中需要填写或选择的字段
        fields = ['text','public']
        # 设置每个输入框上侧的标签
        labels = {'text': 'topic', 'public': 'is public'}

class EntryForm(forms.ModelForm):
    """条目表"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
