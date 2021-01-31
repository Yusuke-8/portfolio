from django.db import models
from mdeditor.fields import MDTextField # 追加
from taggit.managers import TaggableManager
 
class Article(models.Model):
    title = models.CharField(verbose_name='タイトル',max_length=40)
    content = MDTextField(verbose_name='本文')
    snippet = models.CharField(verbose_name='スニペット',max_length=70, default="", editable=True)
    tags = TaggableManager(verbose_name='タグ',blank=True)
    created_at = models.DateTimeField(verbose_name='作成時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)
    release = models.BooleanField(verbose_name='公開')

    class Meta:
        verbose_name_plural = 'ブログ-コンテンツ'

    def __str__(self):
        return self.title