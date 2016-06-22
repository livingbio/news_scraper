from django.core.management.base import BaseCommand
from scraper_app.models import Article
from ...models import SegmenterEvaluateResult
from ...libs.segmenter import EvaluateJieba, EvaluateMix, EvaluateMaster, EvaluateStanford


class Command(BaseCommand):
    help = 'Evaluate different segmenter by news data from LTN news'

    def evalute(self, model, articles):
        score = 0.0
        for a in articles:
            keywords = [kw for kw in a.keyword.split(',') if len(kw) <= 3 and len(kw) >= 2]
            if len(keywords) > 0:
                score += model.test(a.text, keywords)
        return score / len(articles)

    def handle(self, *args, **options):
        articles = Article.objects.all()
        jieba = EvaluateJieba()
        mix = EvaluateMix()
        master = EvaluateMaster()
        stanford = EvaluateStanford()

        jieba_score = self.evalute(jieba, articles)
        result = SegmenterEvaluateResult(name='jieba', precision=jieba_score)
        result.save()
        print 'jieba score', jieba_score

        mix_score = self.evalute(mix, articles)
        result = SegmenterEvaluateResult(name='mix jieba and master', precision=mix_score)
        result.save()
        print 'mix score', mix_score

        master_score = self.evalute(master, articles)
        result = SegmenterEvaluateResult(name='master', precision=master_score)
        result.save()
        print 'master score', master_score

        stanford_score = self.evalute(stanford, articles)
        result = SegmenterEvaluateResult(name='stanford', precision=stanford_score)
        result.save()
        print 'stanford score', stanford_score
