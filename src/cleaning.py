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

#Find any missing values for borough
def find_borough(df) :  

    #create a df with only borough and locaton
    df_out = df[['borough','location']] 

    #delete row with no element
    df_out = df_out.dropna()

    #delete duplicates data 
    df_out = df_out.drop_duplicates(subset=None, keep='first', inplace=False) #drop duplicate data 

    #create a dictionnary with location as index with df_out from location and borough
    dic = pd.Series(df_out.borough.values,index=df_out.location).to_dict()

    # map the values on the dataframe
    df["borough"] = df["location"].map(dic)

    return df 

def find_on_street_name(df) :  

    #create a df with only on_street_name and locaton
    df_out = df[['on_street_name','location']] 

    #delete row with no element
    df_out = df_out.dropna()

    #delete duplicates data 
    df_out = df_out.drop_duplicates(subset=None, keep='first', inplace=False) #drop duplicate data 

    #create a dictionnary with location as index with df_out from location and on_street_name
    dic = pd.Series(df_out.on_street_name.values,index=df_out.location).to_dict()

    # map the values on the dataframe
    df["on_street_name"] = df["location"].map(dic)

    return df 
