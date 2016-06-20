# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem
import json


class Website(models.Model):
    name = models.CharField(max_length=200)     # 分類的名稱
    url = models.URLField()                     # 主要的網址
    # ForeignKey是多對一的關係，多個Website可以同時被一個Scraper管理
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    # SchedulerRuntime會管理每一個Website
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)   # 文章的標題
    news_website = models.ForeignKey(Website)  # 每篇文章一定會屬於一個Website
    description = models.TextField(blank=True) # 文章的內容
    url = models.URLField()                    # 文章的URL
    keyword = models.CharField(max_length=200) # 關鍵字, 用json.dumps(list)儲存
    # SchedulerRuntime會管理所有的Article
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title


class ArticleItem(DjangoItem):
    django_model = Article

