import pandas as pd
import numpy as np

from src.cleaning import *

df = pd.read_csv('data/data_100000.csv')
print(df.isnull().sum())

#exploring_data(df)
df = clean_data(df)

df = find_borough(df)

df = find_on_street_name(df)

print(df.isnull().sum())


