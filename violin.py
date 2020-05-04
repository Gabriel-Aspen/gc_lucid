import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.manifold import TSNE

def numeric(df, target=None, dimensions=[5,5]): #make appropriate dimensions
    '''Create violin plots for all other variables plotted against a target
        variable

    Attributes:
        df (pd DataFrame) represents a dataframe of all data and labels
        target (str) represents the column name of the label
        dimensions(list) represents layout of all the plots (rows, columns)

        Problems:
            1. 'dimensions' should be set automaticaly, find a way to do this
    '''
    oe = OrdinalEncoder()
    #separate out the numeric target so it doesn't get encoded
    non_target_columns = list(set(df.columns)-set(target))
    ordinal_array = oe.fit_transform(df[non_target_columns])
    ordinal_df = pd.DataFrame(ordinal_array, columns=non_target_columns)
    #add the target back untouched
    ordinal_df[target] = df[target]

    plt.figure(figsize=(20,16))
    for i, col in enumerate(list(ordinal_df.columns.values)):
        plt.subplot(5,5,i+1)
        sns.violinplot(x=target, y=col, data=ordinal_df)
        plt.grid()
        plt.tight_layout()

def categorical(df, target=None, dimensions=[5,5]): #make appropriate dimensions
    '''Create violin plots for all other variables plotted against a target
        variable

    Attributes:
        df (pd DataFrame) represents a dataframe of all data and labels
        target (str) represents the column name of the label
        dimensions(list) represents layout of all the plots (rows, columns)

        Problems:
            1. 'dimensions' should be set automaticaly, find a way to do this
            2. Target variable is being encoded to a number, sns breaks if we
                don't do this
    '''
    oe = OrdinalEncoder()
    #allow the target to be assigned a number
    ordinal_array = oe.fit_transform(df)
    ordinal_df = pd.DataFrame(ordinal_array, columns = df.columns)

    plt.figure(figsize=(20,16))
    for i, col in enumerate(list(ordinal_df.columns.values)):
        plt.subplot(5,5,i+1)
        sns.violinplot(x=target, y=col, data=ordinal_df)
        plt.grid()
        plt.tight_layout()
