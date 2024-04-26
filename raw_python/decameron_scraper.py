# ok first some imports
import pyvis as pv 
import networkx as nx 
import pandas as pd
import requests
import scipy
from bs4 import BeautifulSoup
from pyvis.network import Network

import requests
import os
import re
import numpy as np
import gensim
import gensim.corpora as corpora

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from pprint import pprint
from bs4 import BeautifulSoup
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel

## many thanks to this website: https://bennett-holiday.medium.com/a-step-by-step-guide-to-writing-an-lda-program-in-python-690aa99119ea

def clean_story(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="container")
    main_text = results.find_all("p")

    full_story = ""
    for element in main_text:
        clean_element = element.text.strip()
        clean_element = re.sub(r'[0-9]+', '', clean_element)
        clean_element = re.sub(r'\[|\]|\t|\n', '', clean_element)
        full_story += clean_element
    return full_story

def two_digit(digit):
    if (digit < 10):
        digit = f"0{digit}"
    return str(digit)

def return_URL(day, story):
    story = two_digit(story)
    day = two_digit(day)
    URL = f"https://www.brown.edu/Departments/Italian_Studies/dweb/texts/DecShowText.php?myID=nov{day}{story}&lang=eng"
    return URL

def analyze_story():
    #TODO
    return

# some NLP?
print("loading dataset")


day = 1
day_all = ""

# this creates a 2d array of all the stories
stories_all = []
for day in np.arange(1, 11, 1):
    day_stories = []
    for story in np.arange(1, 11, 1):
        print(f"Currently Scraping: Day {day}, Story {story}")
        day_stories.append(clean_story(return_URL(day, story)))
    stories_all.append(day_stories)


stop_words = stopwords.words("english")
annoying_words = ["thou", "one", "said", "thy", "tis", "thee"]
stops_words = stop_words.append(annoying_words)
texts = [[word for word in simple_preprocess(str(story)) if word not in stop_words] for story in stories_all]

id2word = corpora.Dictionary(texts)
corpus = [id2word.doc2bow(text) for text in texts]
#num_topics = 10
lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=3, random_state=42, passes=50, alpha="auto", per_word_topics=True)

pprint(lda_model.print_topics())