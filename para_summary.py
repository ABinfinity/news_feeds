# -*- coding: utf-8 -*-
"""
Created on Thu Aug 1 15:48:39 2018

@author: Abinfinity
"""


# producing summary of the news article

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 5

class para():
    def summ(url):
        # url = "https://www.hindustantimes.com/tech/samsung-galaxy-note-9-launch-live-full-specifications-features-and-more/story-heLEeZMY2rl2j55Wd5LWgP.html"
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        summary = " "
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
        	summary = summary+str(sentence)

        return summary






