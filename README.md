#GC Lucid
Our version of a turnkey data visualization package

## Required modules
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib

##Functions
- tsnetools.py: Quickly generate a 2d tsne plot of a dataset. Specify a target
                to color the plot by. Target can be categorical or numeric
                numeric_tsne()
                categorical_tsne()
- violin.py: Create violin plots for all other variables plotted against a target
                variable
                numeric()
                categorical()
