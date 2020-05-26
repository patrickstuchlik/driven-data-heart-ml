import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/heart/heart.dat'

heart = pd.read_fwf(url)
heart.head()