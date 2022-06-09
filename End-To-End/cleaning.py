import pandas as pd
import re

def clean_dataset(data):
  data_clean = data.copy(deep=True)
  for i in range(len(data_clean.columns)):
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&apos;', '\'', x))
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&quot;', '\"', x))
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&#124;', '|', x))
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&#93;', ']', x))
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&#91;', '[', x))
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&gt;', '>', x))
    data_clean.iloc[:,i] = data_clean.iloc[:,i].apply(lambda x: re.sub('&lt;', '<', x))

  return data_clean
