# !/usr/bin/python
# -*- coding: utf-8 -*-

from summarizer import Summarizer


class TextTeaser(object):

    def __init__(self):
        self.summarizer = Summarizer()

    def summarize(self, title, text, category="Undefined", source="Undefined", count=5):
        result = self.summarizer.summarize(text, title, source, category)
        result = self.summarizer.sortSentences(result[:count])
        result = [res['sentence'] for res in result]

        return result
