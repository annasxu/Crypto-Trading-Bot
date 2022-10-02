from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost import XGBRegressor



def model(dataframe):
  df = dataframe
  #clean up X and Y, variable to add back later 
  X = df.drop(columns=['PumpTom?','coin','date','%changeTom','close_time'])
  Y = df["PumpTom?"].to_list()
  #split X and Y into training and test 
  train_cut = 0.8
  x_train = X[:int(X.shape[0]*train_cut)]
  x_test = X[int(X.shape[0]*train_cut):]
  y_train = Y[:int(X.shape[0]*train_cut)]
  y_test = Y[int(X.shape[0]*train_cut):]
  test_coin = df['coin'][int(X.shape[0]*train_cut):]
  #fit the model to the training X and training Y 
#   model = XGBRegressor()
#   model.fit(x_train, y_train)
#   y_pred = model.predict(x_test)
#   x_test['pump_prob'] = y_pred
#   x_test['coin'] = test_coin
#   backtestdf = x_test
#   backtestdf['PumpTom?'] = y_test  
  rf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0)
  rf.fit(x_train, y_train)
  y_pred = rf.predict(x_test)
  threshold = 0.2
  predicted_proba = rf.predict_proba(x_test)
  predicted = (predicted_proba [:,1] >= threshold).astype('int')
  pump_prob = [true_prob[1] for true_prob in predicted_proba]
  x_test['pump_prob'] = pump_prob
  x_test['coin'] = test_coin
  backtestdf = x_test
  backtestdf['PumpTom?'] = y_test
  sorted_timestamp = set(df['timestamp'])
  sorted_timestamp.remove(max(sorted_timestamp))
  timestamp= max(sorted_timestamp)
  recco = backtestdf[backtestdf['timestamp'] == timestamp].sort_values(by=['pump_prob']).tail(n=2)
  coin_recco = recco['coin'].values
  return coin_recco



