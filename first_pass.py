import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def initial_text(df):
	'''

	Printing the first few commmands a notebook typically starts with
	1. first 5 rows
	2. column types
	3. Relative NaN values
	4. Show numeric and categorical columns, then assign to variables

	'''
	print("First five rows:")
	print(df.head())
	print("/n/n")

	print("Column types:")
	print(df.info())
	print("/n/n")

	print("Columns with 30/% or more NaNs:")
	# TODO: loop through columns, generate list where
	# 50% or more of df.shape[0] is null
	# print list
	print("/n/n")

	print("Set numeric columns to df_numerics_list")
	df_numerics_list = df.select_dtypes(include=np.number).columns.tolist()
	print(df_numerics_list, "/n/n")

	print("Set categorical columns to df_cat_list")
	df_cat_list = df.select_dtypes('category').columns.tolist()
	print(df_cat_list, "/n/n")



def initial_plot(df):
	'''
	Printing first pass plots
	'''
	plt.figure(figsize=(12,10))

	print("Correlations")
	sns.pairplot(data=df)
	print("/n/n")


	print("Correlation heat matrix, if 0.5 or higher, or -0.4 or lower:")
	df_corr = df.corr()
	sns.heatmap(df_corr[(corr >= 0.5) | (corr <= -0.4)],
		annot=True, annot_kws={"size": 8}, square=True)