import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/heart/heart.dat'

heart = pd.read_csv(url,sep='\s+', names = ['age','sex','pain','bp','cholesterol','sugar','ecg','hr','angina','oldpeak','slope','vess','thal','disease'])
print(heart.head())