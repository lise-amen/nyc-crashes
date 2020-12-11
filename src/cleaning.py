import numpy as np
import pandas as pd

def exploring_data(df) : 
    print(df.info()) # Index, Datatype and Memory information
    missing_values_count = df.isnull().sum()
    print(missing_values_count) #number missing values

def clean_data(df) :
    df = df.drop_duplicates(subset=None, keep='first', inplace=False) #drop duplicate data 
    df = df[df['location'].notna()]
    
    return df 

#find any missing value with location as target
def find_datas_with_localite(df, df_out, column_name) :  
    
    #delete row with no element
    df_out = df_out.dropna()

    #delete duplicates data 
    df_out = df_out.drop_duplicates(subset=None, keep='first', inplace=False) #drop duplicate data 

    #create a dictionnary with location as key value 
    name_list = df_out[column_name].tolist()
    location_list = df_out['location'].tolist()
    dic = dict(zip(location_list, name_list))

    # map the values on the dataframe
    df[column_name] = df["location"].map(dic)

    return df 

# replace nan values in the dataset by 'Unspecified' in contributing_factor_vehicule columns 
def replace_nan_value(df) :

    df[['contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4', 'contributing_factor_vehicle_5']] = df[['contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4', 'contributing_factor_vehicle_5']].fillna('Unspecified')

    return df 
