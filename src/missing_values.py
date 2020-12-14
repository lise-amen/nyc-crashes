import numpy as np
import pandas as pd

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

