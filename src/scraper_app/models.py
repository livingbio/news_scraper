# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from scrapy_djangoitem import DjangoItem
import json


class Article(models.Model):
    title = models.CharField(max_length=200)   # 文章的標題
    text = models.TextField(blank=True)        # 文章的內容
    url = models.URLField()                    # 文章的URL
    keyword = models.CharField(max_length=200) # 關鍵字, 用json.dumps(list)儲存

    def __unicode__(self):
        return self.title


class ArticleItem(DjangoItem):
    django_model = Article

