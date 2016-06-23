[![Build Status](https://travis-ci.org/livingbio/django-template.svg?branch=master)](https://travis-ci.org/livingbio/django-template)

# Evaluation of Chinese Segmenters

Evaluate four Chinese segmenters: [jieba](https://github.com/fxsjy/jieba), jieba with pre-defined dictionary, 大師's dictionary-based segmenter, [Stanford segmenter](http://nlp.stanford.edu/software/segmenter.shtml).

### Setting Virtualenv

At first, you should make sure you have [virtualenv](http://www.virtualenv.org/) installed.

    cd news_scraper
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Setting up local environment variables

Settings are stored in environment variables via [django-environ](http://django-environ.readthedocs.org/en/latest/). The quickiest way to start is to copy and rename `local.sample.env` into `local.env`:

    cp src/news_scraper/settings/local.sample.env src/news_scraper/settings/local.env

Then edit the SECRET_KEY in local.env file, replace `q+#ae^hxgz7o*lvdatnsu76365uwmspc$(vac%9(b8gck-(l^z` into any [Django Secret Key](http://www.miniwebtool.com/django-secret-key-generator/), for example:

    SECRET_KEY=twvg)o_=u&@6^*cbi9nfswwh=(&hd$bhxh9iq&h-kn-pff0&&3


### Run web server

After that, just cd to `src` folder:

    cd src

And run migrate and http server:

    python manage.py migrate
    python manage.py runserver


### Scrape news for evaluation

It takes about 10 minutes to scrape news from LTN news.

    cd src
    scrapy crawl news.ltn.com.tw


### Evaluate segmenters

    python manage.py eval_segmenter

