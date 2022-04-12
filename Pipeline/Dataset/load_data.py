# Load the PIE data from the file into the required Pandas DataFrame format.
# The file 'data_cleaned.csv' is the dataset downloaded from GitHub, although it might be better to rename it to avoid
# confusion.

import pandas as pd

df = pd.read_csv ('data_cleaned.csv')
data = pd.DataFrame({"prefix": "", "input_text": df.loc[:,"Idiomatic_Sent"], "target_text": df.loc[:,"Literal_Sent"]})

print(data.iloc[0:3,:])  # Show example

