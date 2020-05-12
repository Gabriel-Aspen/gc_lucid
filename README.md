# GC Lucid
See visual.ipynb for examples
## Required modules
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- plotly

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
Using random forest, will print and return feature importances
### first_pass.py
Printing the first few commands a notebook typically starts with
1. first 5 rows
2. column types
3. Relative NaN values
4. Show numeric and categorical columns, then assign to variables
### corrplot.py
Generates a correlation heatmap of all features
### datasets.py
Calling a function returns a pd DataFrame of a pre-selected dataset
- wine quality
- voting records
- mushroom attributes
- yeast protein localization sites
### nulls.py
Display null counts using plotly bar chart
