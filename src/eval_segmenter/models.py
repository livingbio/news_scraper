from django.db import models


class SegmenterEvaluateResult(models.Model):
    name = models.CharField(max_length=30)
    precision = models.FloatField()

    def __unicode__(self):
        return '{}: {}'.format(self.name, self.precision)

