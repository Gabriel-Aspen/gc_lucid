# GC Lucid
See visual.ipynb for examples
## Required modules
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

## Functions
### tsnetools.py
Generates a 2d tsne plot of a dataset. Plot is colored by label (y)
- numeric_tsne()
- categorical_tsne()
### violin.py
Create violin plots for each condition of the label (y) for all features simultaneously
- numeric()
- categorical()
### feature_importance.py
Using random forest, will return feature importances
1. first 5 rows
2. column types
3. Relative NaN values
4. Show numeric and categorical columns, then assign to variables
### datasets.py
Calling one of the functions returns a pd DataFrame of a pre-selected dataset
- wine() - wine quality
- voting() - voting records
- mushroom() - mushroom attributes
- yeast() - yeast protein localization sites
