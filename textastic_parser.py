"""
Parsers to support the Textastic Framework

TAKEN FROM LECTURE
"""

import json
from collections import Counter
import re
import string
from textblob import TextBlob


def json_parser(filename):
    f = open(filename)
    raw = json.load(f)
    text = raw['speech']

    # sentences
    sentence_endings = re.compile(r'[.!?]')
    sentences = sentence_endings.split(text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    # words
    words = text.split(" ")
    words = [''.join(filter(str.isalnum, word.lower())) for word in words]
    words_no_space = [s for s in words if s != '']

    # word count
    wc = Counter(words_no_space)
    num = len(wc)

    #sentence length
    avg_sentence_length = len(words_no_space) / len(sentences) if len(sentences) > 0 else 0

    # sentiment
    words = ' '.join(words)
    blob = TextBlob(words)
    sent_score = blob.sentiment.polarity

    f.close()
    return {'wordcount': wc, "avg_sentence_length": avg_sentence_length, 'sent_score': sent_score, 'numwords':num}