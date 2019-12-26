import os 
import pandas as pd

def fix_timezones(csv_path:str)->pd.DataFrame:
  """
  Basic function to fix intial data bug 
  related to NaN values in non-eastern-time zones due 
  to UTC conversion.
  """
  df = pd.read_csv(csv_path)
  the_count = df[0:2]['cfs'].isna().sum()
  return df[the_count:]

def split_on_na_chunks(df:pd.DataFrame):
  pass 

def interpolate_missing_values(df:pd.DataFrame)->pd.DataFrame:
  """
  Function to fill missing values with nearest
  value. Should be run only after splitting on the NaN
  chunks.
  """
  df['cfs1'] = df['cfs'].interpolate(method='nearest')
  df['precip'] = df['p01m'].interpolate(method='nearest')
  df['temp'] = df['tmpf'].interpolate(method='nearest')
  return df