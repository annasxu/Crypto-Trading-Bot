import pandas as pd
import numpy as np
from ta import add_all_ta_features
from datetime import timedelta, datetime  
from ta import add_all_ta_features
from ta.utils import dropna

def add_indicators(dataframe):
  df = dataframe
  df['date'] = pd.to_datetime(df['timestamp'], unit = 'ns')
  df = add_all_ta_features(df, open="open", high="high", low="low", close="close", volume="volume")
  df['%change'] = (df['close']-df['open'])/df['open']
  df['%changeTom'] = df['%change'].shift(-1)
  df['Pump?'] = np.where(df['%change'] > .08, True, False)
  df['PumpTom?'] = df['Pump?'].shift(-1)
  df = df[df.timestamp != min(df['timestamp'])]
  #fixing the timestamp min
  new_data = pd.DataFrame()
  for i in df['coin'].unique():
    coindf = df.loc[df['coin'] == i]
    coindf = coindf[coindf.timestamp != min(coindf['timestamp'])]
    coindf = coindf[coindf.timestamp != max(coindf['timestamp'])]
    new_data = new_data.append(coindf)
  df = new_data
  df = df.sort_values(by=['timestamp','coin'])
  df = df.replace([np.inf, -np.inf], np.nan)
  df = df.fillna(0)
  return df