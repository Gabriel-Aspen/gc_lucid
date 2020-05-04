from sklearn.ensemble import RandomForestClassifier

'''
inputs:
x = dataframe of input columns
Y = dataframe of target column
'''

def feature_importance(x, y):

	rfc = RandomForestClassifier()

	names = x.columns.values

	rfc.fit(x,Y)

	print("Features sorted by importance: ")
	print(sorted(zip(map(lambda x: round(x, 4), rfc.feature_importances_), names, reverse=True)))


