'''
File: sankey.py
Description: plots sankey given dataframe
Author: Sarah Klute
'''
import plotly.graph_objects as go
import pandas as pd



def _code_mapping(df, src, targ):
    '''
    Code maps the nodes in the sankey diagram
    :param df: dataframe
    :param src: source column from dataframe
    :param targ: target column from dataframe
    :return: df (dataframe), labels (list) for nodes and links of sankey
    '''

    # get the distinct labels from src/targ columns
    labels = list(set(list(df[src]) + list(df[targ])))

    # generate n integers for n labels
    codes = list(range(len(labels)))

    # create a map from label to code
    lc_map = dict(zip(labels, codes))

    # substitute names for codes in the dataframe
    df = df.replace({src:lc_map, targ:lc_map})

    # Return modified dataframe and list of labels
    return df, labels


def make_sankey(df, *cols,  save=None, **kwargs):
    '''
    make the sankey diagram based on specified attributes
    :param df: dataframe
    :param cols: specified columns in a list
    :param vals: values associated iwth columns, defaul None
    :param save: if saving the figure
    :param kwargs:
    :return: Sankey diagram
    '''
    stacked = df
    stacked.drop('values', axis=1)

    # assigning values to stacked columnds
    src, targ, values = stacked.columns

    # code mapping for sankey
    stacked, labels = _code_mapping(stacked, src, targ)

    # making sankey:
    link = {'source': stacked[src].astype(str), 'target': stacked[targ].astype(str), 'value': stacked[values],
        'line':{'color':'black', 'width':1}}

    node_thickness = kwargs.get("node_thickness", 50)

    node = {'label': labels, 'pad':50, 'thickness':node_thickness,
        'line':{'color':'black', 'width':1}}

    skf = go.Sankey(link=link, node=node)
    fig = go.Figure(skf)

    fig.show()

    if save:
        fig.write_image(save)



