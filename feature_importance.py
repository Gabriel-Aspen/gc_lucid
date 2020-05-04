from sklearn.ensemble import RandomForestClassifier


def feature_importance(x, y):

	'''
	Using random forest, will return feature importances

	Attributes:
	x = dataframe of input columns
	Y = dataframe of target column

	Output:

	Features sorted by their score:
	[(0.570, 'col1'), (0.351, 'col2'), .. etc..]
	'''

	rfc = RandomForestClassifier()

	names = x.columns.values

	rfc.fit(x,Y)

	print("Features sorted by importance: ")
	print(sorted(zip(map(lambda x: round(x, 4), rfc.feature_importances_), names, reverse=True)))


