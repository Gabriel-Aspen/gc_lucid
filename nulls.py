import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

''' Notes:
    - Make an option for percent missing

'''

def make_nulldf(df):
    '''
    Turn df.isnull().sum() into a dataframe

    Attribute:
        df: The pd DataFrame of interest

    Output:
        A DataFrame showing the sum of null values for each column. Columns = ['attribute', 'counts']
    '''
    null_df = pd.DataFrame(df.isnull().sum().reset_index())
    null_df.columns = ['attribute', 'counts']
    return null_df

def null_plot(df):
    '''Plot nulls using plotly

    Attribute:
        df: The pd DataFrame of interest

    Output:
        plotly bar chart of null counts for each column
    '''
    null_df = make_nulldf(df)
    fig = px.bar(null_df, x='attribute', y='counts')
    fig.show()
