# ok first some imports
import pyvis as pv 
import networkx as nx 
import pandas as pd
from pyvis.network import Network

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

# read in data and create graph
df = pd.read_csv("decameron_themes.csv")
main_graph = Network(directed = True)
main_graph.set_edge_smooth("dynamic")

for index, row in df.iterrows():
    #TODO: add color in here based on storyteller
    main_graph.add_node(row["Story_Hash"], label = f"Day {row["Day"]}, Story {row["Story"]}", color = storytellers[row["Storyteller"]])


# creating theme lists
THEMES = ["Storytelling", "Cultural_Exchange", "Sexuality"]
theme_dict = {}
color_coding = {
    "Storytelling" : "blue",
    "Cultural_Exchange" : "green",
    "Sexuality" : "red"
}
for theme in THEMES:
    theme_dict[theme] = df.loc[df[theme] == True]["Story_Hash"].tolist()
    connect_edges(theme_dict[theme], main_graph, color_coding[theme])



main_graph.show_buttons()
main_graph.show("hello.html")