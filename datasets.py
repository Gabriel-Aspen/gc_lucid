import numpy as np
import pandas as pd

'''Calling a function returns a pd Dataframe of a chosen dataset:

    wine (numeric)
        columns: particular attributes of wine (density, alcohol, etc.)
        target: quality rating given by wine experts

    votes (boolean - y/n)
        columns: Particular bills (immigration, education spending, etc.)
        target: republican (1) or not (0)

    mushroom (categorical)
        columns: Logical rules for mushroom identification
                (cap shape, spore print  color, etc.)
        target: poisonous (1) or edible (0)

    yeast (categorical/numeric)
        columns: ** Complicated, see below**
        target: Location site of protein (nucleus, mitochondria, etc.)
'''
def wine():
    wine_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    data = pd.read_csv(wine_url, sep=';')
    data.columns = data.columns.str.replace(' ', '_')
    return data

def votes():
    votes_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/voting-records/house-votes-84.data'
    data = pd.read_csv(votes_url, sep=',')
    data.columns = data.columns.str.replace(' ', '_')
    return data

def mushroom():
    mushroom_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
    data = pd.read_csv(mushroom_url, sep=',')
    data.columns = data.columns.str.replace(' ', '_')
    return data

def yeast():
    yeast_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/yeast/yeast.data'
    data = pd.read_csv(yeast_url, sep= "\s+",
                   names=['Sequence_name', 'mcg', 'gvh', 'alm', 'mit', 'erl', 'pox',
                          'vac', 'nuc', 'Site'])
    return data
