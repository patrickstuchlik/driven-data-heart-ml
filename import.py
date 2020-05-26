import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/heart/heart.dat'

heart = pd.read_csv(url,sep='\s+', names = ['age','sex','pain','bp','cholesterol','sugar','ecg','hr','angina','oldpeak','slope','vess','thal','disease'])

heart[['age','sex','pain','sugar','ecg','angina','slope','vess','thal']] = heart[['age','sex','pain','sugar','ecg','angina','slope','vess','thal']].astype(int)

print(heart.head())