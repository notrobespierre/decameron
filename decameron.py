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

## FUNCTIONS

def add_edges_rey(graph, edges):
    """
    This method serves to add multiple edges between existing nodes
    in the network instance. Adding of the edges is done based off
    of the IDs of the nodes. Order does not matter unless dealing with a
    directed graph.

    :param edges: A list of tuples, each tuple consists of source of edge,
                  edge destination and and optional width.

    :type arrowStrikethrough: list of tuples
    """
    for edge in edges:
        # if incoming tuple contains a weight
        if len(edge) == 3:
            graph.add_edge(edge[0], edge[1], color=edge[2], arrows = "hi")
        else:
            graph.add_edge(edge[0], edge[1])


def connect_edges(edges_list, graph, color):
    connect_list = [(story1, story2, color) for story1 in edges_list for story2 in edges_list if story1!=story2 and story1>story2]
    print(connect_list)
    add_edges_rey(graph, connect_list)

def return_URL(day, story):
    story = two_digit(story)
    day = two_digit(day)
    URL = f"https://www.brown.edu/Departments/Italian_Studies/dweb/texts/DecShowText.php?myID=nov{day}{story}&lang=eng"
    return URL


## DICTIONARIES AND DATA

# creating storytellers colors
storytellers = {
    "Panfilo" : "#9e0142",
    "Neifile" : "#d53e4f",
    "Filomena" : "#f46d43",
    "Dioneo" : "#fdae61",
    "Fiametta" : "#fee08b",
    "Emilia" : "#e6f598",
    "Filostrato" : "#abdda4",
    "Lauretta" : "#66c2a5",
    "Elissa" : "#3288bd",
    "Pampinea" : "#5e4fa2"
}

# themes

THEMES = ["Storytelling", "Cultural_Exchange", "Sexuality", "Gender_Bending"]
theme_dict = {}
color_coding = {
    "Storytelling" : "blue",
    "Cultural_Exchange" : "green",
    "Sexuality" : "red",
    "Gender_Bending": "purple"
}


## ACTUAL STUFF
# read in data and create graph
df = pd.read_csv("decameron_themes.csv")
main_graph = Network(directed = True)
main_graph.set_edge_smooth("dynamic")

for index, row in df.iterrows():

    # this adds nodes to the graphs of each of the storytellers
    main_graph.add_node(row["Story_Hash"], label = f"Day {row["Day"]}, Story {row["Story"]}", color = storytellers[row["Storyteller"]])
    
    # TODO main_graph[row[""]= 
    #


# creating theme lists
for theme in THEMES:
    theme_dict[theme] = df.loc[df[theme] == True]["Story_Hash"].tolist()
    connect_edges(theme_dict[theme], main_graph, color_coding[theme])


## OK LETS SEE THIS
main_graph.barnes_hut(spring_length = 150)
#main_graph.show_buttons()
main_graph.show("graph.html")