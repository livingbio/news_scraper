# -*- coding: utf-8 -*-
import os
import string


class CWSegmenter(object):
    DICT_PATH = os.path.join(os.path.dirname(__file__), '../data/cw_dict.txt')

    def __init__(self, dictionary=None):
        """The dictioanry can be customized."""
        if dictionary:
            self.dictionary = dictionary
        else:
            self.dictionary = set()
            with open(self.DICT_PATH) as fin:
                for c in fin:
                    self.dictionary.add(c.strip())
        self.longest = max((len(c) for c in self.dictionary))
        self.punctuation_marks = set(string.punctuation)

    def _is_punctuation(self, c):
        # CJK punctuation marks
        if (0x3000 <= ord(c) <= 0x303F) or (0xFF00 <= ord(c) <= 0xFFEF):
            return True
        # ASCII punctuation marks
        if c not in ["-", "/"] and c in self.punctuation_marks:
            return True
        return False

    def longest_match(self, text, pos):
        #   Always split punctuations.
        if self._is_punctuation(text[pos:pos + 1]):
            return 1
        for l in range(self.longest, 0, -1):
            if text[pos:pos + l] in self.dictionary:
                return l
        return 0

    def segment(self, text):
        results = []
        oov = ""
        i = 0
        while i < len(text):
            l = self.longest_match(text, i)
            if l == 0:
                oov += text[i:i + 1]
                i += 1
            else:
                if oov:
                    results.append(oov.strip())
                    oov = ""
                results.append(text[i:i + l])
                i += l
        if oov:
            results.append(oov.strip())
        return results
