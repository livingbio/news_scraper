from eval_segmenter.libs.conv2cn import Conv2Cn
from eval_segmenter.libs.cwsegment import CWSegmenter
from suds.client import Client
from jieba import Tokenizer
import os


class EvaluateJieba(object):
    def __init__(self):
        self.jieba = Tokenizer()

    def test(self, text, keywords):
        seg_text = list(self.jieba.cut(text))
        total = 0
        correct = 0
        for kw in keywords:
            total += text.count(kw)
            correct += seg_text.count(kw)
        if total == 0:
            return 0.0
        return float(correct) / total


class EvaluateMix(object):
    def __init__(self):
        self.jieba = Tokenizer()
        master_dict = os.path.join(os.path.dirname(__file__), '../data/cw_dict.txt')
        self.jieba.load_userdict(master_dict)

    def test(self, text, keywords):
        seg_text = list(self.jieba.cut(text))
        total = 0
        correct = 0
        for kw in keywords:
            total += text.count(kw)
            correct += seg_text.count(kw)
        if total == 0:
            return 0.0
        return float(correct) / total


class EvaluateMaster(object):
    def __init__(self):
        self.seg = CWSegmenter()

    def test(self, text, keywords):
        seg_text = self.seg.segment(text)
        total = 0
        correct = 0
        for kw in keywords:
            total += text.count(kw)
            correct += seg_text.count(kw)
        if total == 0:
            return 0.0
        return float(correct) / total


class EvaluateStanford(object):
    def __init__(self):
        self.seg = Client('http://localhost:9999/seg?wsdl').service.getSegmentResult
        self.conv = Conv2Cn().conv

    def test(self, text, keywords):
        text = self.conv(text)
        seg_text = self.seg(text).split()
        total = 0
        correct = 0
        for kw in keywords:
            total += text.count(self.conv(kw))
            correct += seg_text.count(self.conv(kw))
        if total == 0:
            return 0.0
        return float(correct) / total
