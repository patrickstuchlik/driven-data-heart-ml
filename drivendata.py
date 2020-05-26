import pandas as pd
train_x = pd.read_csv('train_values.csv')
train_y = pd.read_csv('train_labels.csv')
test_x = pd.read_csv('test_values.csv')
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier

est = [('ss',StandardScaler()),('sgd',SGDClassifier())]
pipe = Pipeline(est)

pipe.fit(train_x.iloc[:,1:],train_y)
