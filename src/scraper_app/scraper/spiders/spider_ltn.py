# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scraper_app.models import ArticleItem
from datetime import date, timedelta
import json


class LTN_Spider(Spider):

    name = 'news.ltn.com.tw'
    allowed_domains = ['news.ltn.com.tw']
    start_day = date(2014, 10, 1)
    types = ['focus']  # , 'politics', 'society'

    def url_type_date(self, typ, dat):
        return 'http://{}/newspaper/{}/{}'. \
               format(self.name, typ, dat.strftime('%Y%m%d'))

    def url_path(self, rel_path):
        return 'http://{}/{}'.format(self.name, rel_path)

    def start_requests(self):
        one_day = timedelta(days=1)
        d = self.start_day
        while True:
            for t in self.types:
                yield Request(self.url_type_date(t, d), self.parse)
            d = d + one_day
            if d >= date.today():
                break

    def parse(self, response):
        # follow每一個新聞連結
        for path in response.xpath('//ul[@id="newslistul"]//a/@href').extract():
            yield Request(self.url_path(path), self.parse_news)

        # 檢查是否有下一頁
        for page in response.xpath('//strong[@class="p_num"]/following-sibling::a[1]/@href').extract():
            yield Request(self.url_path(page), self.parse)

    def parse_news(self, response):
        text = []
        for paragraph in response.xpath('//div[@id="newstext"]/p/text()').extract():
            text.append(paragraph)
        text = u'\n\n'.join(text)
        keywords = response.xpath('//div[@class="con_keyword boxTitle"]/a/text()').extract()
        title = response.xpath('//h1/text()').extract_first()

        item = ArticleItem()
        item['title'] = title
        item['text'] = text
        item['url'] = response.url
        item['keyword'] = u','.join(keywords)
        item.save()
