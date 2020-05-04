# GC Lucid
Our version of a turnkey data visualization package

## Required modules
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

## Functions
### tsnetools.py
Quickly generate a 2d tsne plot of a dataset. Specify 'target' column of the dataset to color the plot by. Target can be categorical or numeric
- numeric_tsne()
- categorical_tsne()
### violin.py
Create violin plots for all variables using the unique features of the 'target' column as the x axis. For example, if political party was your target column, each plot would have two violins: republican and democrat.
- numeric()
- categorical()
