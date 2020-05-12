from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
'''
Notes:
- May use feature_importance in other functions to find top (10ish) features
- Added a 'return' to make this easier
'''

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

	rfc.fit(x,y)

	print("Features sorted by importance: ")
	print(np.array(sorted(zip(map(lambda x: round(x, 4),
	rfc.feature_importances_), names), reverse=True)))

	return np.array(sorted(zip(map(lambda x: round(x, 4), rfc.feature_importances_), names), reverse=True))
