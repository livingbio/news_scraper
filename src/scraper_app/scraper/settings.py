import os
import django

BOT_NAME = 'news_scraper'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_scraper.settings.local")

django.setup()

SPIDER_MODULES = ['scraper_app.scraper']
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

NEWSPIDER_MODULE = 'scraper_app.scraper.spiders'

ITEM_PIPELINES = {
#    'scraper_app.scraper.pipelines.DjangoWriterPipeline': 800,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

