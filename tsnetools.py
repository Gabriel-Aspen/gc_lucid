import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.manifold import TSNE

def numeric_tsne(df, target=None):
    '''Quickly generate a tsne plot of a dataset

        df (pd DataFrame) represents a dataframe of all data and labels
        target (str) represents the column name of the label
        ordinal(boolean) represents whether an OrdinalEncoder is used to handle
            categorical variables (True) or not (False)
    '''
    t = TSNE()
    tsne_2d = t.fit_transform(df)
    df2 = pd.DataFrame(tsne_2d, columns = ['tsne1', 'tsne2'])
    df2[target] = df[target]
    #choose a column to coordinate by color- very cool
    hues = len(df[target].unique())
    plt.figure(figsize=(16,10))
    sns.scatterplot(
        x="tsne1", y="tsne2",
        hue=target,
        palette=sns.color_palette("hls", hues),
        data=df2,
        legend="full",
        alpha=0.3
    )

def categorical_tsne(df, target=None):
    '''Quickly generate a tsne plot of a dataset

        df (pd DataFrame) represents a dataframe of all data and labels
        target (str) represents the column name of the label
        ordinal(boolean) represents whether an OrdinalEncoder is used to handle
            categorical variables (True) or not (False)
    '''
    t = TSNE()
    enc = OrdinalEncoder()
    ordinal_array = enc.fit_transform(df)
    tsne_2d = t.fit_transform(ordinal_array)

    df2 = pd.DataFrame(tsne_2d, columns = ['tsne1', 'tsne2'])
    df2[target] = df[target]
    #choose a column to coordinate by color- very cool
    hues = len(df[target].unique())
    plt.figure(figsize=(16,10))
    sns.scatterplot(
        x="tsne1", y="tsne2",
        hue=target,
        palette=sns.color_palette("hls", hues),
        data=df2,
        legend="full",
        alpha=0.3
    )
