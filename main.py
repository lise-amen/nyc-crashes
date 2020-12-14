import pandas as pd
import numpy as np
import re

from src.cleaning import *
from src.missing_values import *

#import dataframe
df = pd.read_csv('data/data_100000.csv')

#exploring_data(df)


df = clean_data(df)

#find any missing value for borough', 'on_street_name', 'off_street_name', 'cross_street_name on taget value location 
list = ['borough', 'on_street_name', 'off_street_name', 'cross_street_name', 'zip_code']
target = 'location'

for name in list : 
    df_out = df[[name,target]]
    df = find_datas_with_localite(df,df_out, name)


list = ('vehicle_type_code1','vehicle_type_code2', 'vehicle_type_code_3', 'vehicle_type_code_4', 'vehicle_type_code_5')

for vehicule in list :
    clean_string_vehicle(df[vehicule]) # clean string for each veicle type

# standardize column name
rename_column(df)


