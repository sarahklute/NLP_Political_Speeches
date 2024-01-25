"""
filename: textastic.py
description: An extensible reusable library for text analysis and comparison
THIS IS THE FRAMEWORK THAT WE SHOULD BASE OUR CODE ON

"""

from collections import defaultdict, Counter
import random as rnd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from sankey import make_sankey
import numpy as np
from wordcloud import WordCloud
import seaborn as sns
sns.set(font_scale=0.75)



class Textastic:

    def __init__(self, stopwords=None):
        # string  --> {filename/label --> statistics}
        # "wordcounts" --> {"A": wc_A, "B": wc_B, ....}
        self.data = defaultdict(dict)
        self.stopwords = stopwords

    def _save_results(self, label, results):
        for k, v in results.items():
            self.data[k][label] = v

    @staticmethod
    def _default_parser(filename):
        """ DEMONSTRATION ONLY:
        Extracting word counts and number of words
        as a random number.
        Replace with a real parser that processes
        your input file fully.  (Remove punctuation,
        convert to lowercase, etc.)   """

        results = {
            'wordcount': Counter("to be or not to be".split(" ")),
            'numwords': rnd.randrange(10, 50)
        }
        return results

    def load_text(self, filename, label=None, parser=None):
        """ Registers a text document with the framework
        Extracts and stores data to be used in later
        visualizations. """

        if parser is None:
            results = Textastic._default_parser(filename)
        else:
            results = parser(filename)

        if label is None:
            label = filename

        if self.stopwords:
            words_to_remove = set(results['wordcount'].keys()) & self.stopwords
            for word in words_to_remove:
                del results['wordcount'][word]
            results['numwords'] = sum(results['wordcount'].values())

        # store the results of processing one file
        # in the internal state (data)
        self._save_results(label, results)

    def load_stop_words(self, stopfile):
        with open(stopfile, 'r') as file:
            self.stopwords = set(file.read().split())

    def compare_num_words(self):
        """ A DEMONSTRATION OF A CUSTOM VISUALIZATION
        A trivially simple barchart comparing number
        of words in each registered text file. """

        num_words = self.data['numwords']
        for label, nw in num_words.items():
            plt.bar(label, nw)
            plt.title('Speech Word Count Comparison')
            plt.ylabel('Word Count')
        plt.show()

    def sentiment(self):
        ''' creates a sentiment bar graph '''
        sentiment = self.data['sent_score']
        for label, s in sentiment.items():
            plt.bar(label, s)
            plt.title('Sentiment Comparison')
            plt.ylabel('Sentiment')
        plt.show()

    def generate_sankey_diagram(self, common_words_count=10, chosen_words=None):
        text_word_counts = {}
        num_words = self.data['wordcount']

        for label, word_counts in num_words.items():
            text_word_counts[label] = dict(word_counts.most_common(common_words_count))

        # ls to store DataFrames before concatenation
        sankey_dfs = []

        for text_name, word_counts in text_word_counts.items():
            if chosen_words:
                words_to_include = set(chosen_words)
            else:
                words_to_include = set(word_counts.keys())

            for word, count in word_counts.items():
                if word in words_to_include:
                    new_row = pd.DataFrame({'source': [text_name], 'target': [word], 'values': [count]})
                    sankey_dfs.append(new_row)

        # concatenate DataFrames outside the loop
        sankey_df = pd.concat(sankey_dfs, ignore_index=True)

        # create the Sankey diagram w
        make_sankey(sankey_df, ['source', 'target', 'values'])



    def _generate_wordcloud(self, label):
        '''generates a word cloud for most common words in each text'''
        word_freq = self.data['wordcount'][label]
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
        plt.figure(figsize=(8, 4))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud for {label}')
        plt.show()

    def visualize_wordclouds(self):
        '''visualizes the wordcloud through calling generate wordcloud, loads in data throough keys'''
        for label in self.data['wordcount'].keys():
            self._generate_wordcloud(label)

