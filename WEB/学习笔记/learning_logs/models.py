from django.db import models

from django.contrib.auth.models import User

# 所有自己创建的类都继承了Django下的Models基类，该类定义了模型的基本功能.
class Topic(models.Model):
    """学习主题"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        """"返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
        """主题下的条目"""
        # 与相关的topic建立外键关系，条目会随着相关topic删除而删除
        topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
        text = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)

        # 嵌套Meta类
        class Meta:
            # 暂时未知作用
            verbose_name_plural = 'entries'

        def __str__(self):
            """呈现条目显示的信息"""
            if len(self.text)> 20:
                 return f"{self.text[:20]}..."
            else:
                return self.text

        

