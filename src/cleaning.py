import numpy as np
import pandas as pd

def exploring_data(df) : 
    print(df.info()) # Index, Datatype and Memory information
    missing_values_count = df.isnull().sum()
    print(missing_values_count) #number missing values

def clean_data(df) :
    df = df.drop_duplicates(subset=None, keep='first', inplace=False) #drop duplicate data 
    df = df[df['location'].notna()]
    
    # replace nan values in the dataset by 'Unspecified' in contributing_factor_vehicule columns 
    df[['contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4', 'contributing_factor_vehicle_5']] = df[['contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4', 'contributing_factor_vehicle_5']].fillna('Unspecified')

    return df 
    
def clean_string_vehicle(df) : 
    # capitalize the first character of each word for vehicule type 
    df = df.str.title()

    # standardize the ambulance name for each vehicule type
    df= df.replace('Ambul', 'Ambulance')
    df= df.replace('Ambu', 'Ambulance')
    df= df.replace('Ambulace', 'Ambulance')
    df= df.replace('Amb', 'Ambulance')
    df= df.replace('Ambu', 'Ambulance')
    df= df.replace('Ambulence', 'Ambulance')
    df= df.replace('Almbulance', 'Ambulance')
    df= df.replace('White Ambu', 'Ambulance')

    # standardize the Fire Truck name for each vehicule type
    df= df.replace('4 Dr Sedan', 'Sedan')
    df= df.replace('2 Dr Sedan', 'Sedan')

    # rename E-Sco by E-Scooter
    df= df.replace('E-Sco', 'E-Scooter')

    # rename E-Bike by E-Bik
    df= df.replace('E-Bik', 'E-Bike')
    df= df.replace('E Bike', 'E-Bike')

    # standardize the Fire Truck name for each vehicule type
    df= df.replace('Fire', 'Fire Truck')

    # standardize the Unknow name for each vehicule type
    df= df.replace('Unk', 'Unknown')
    df= df.replace('Unkno', 'Unknown')
    df= df.replace('Unkno', 'Unknown')
    df= df.replace('0', 'Unknown')
    df= df.replace('Unkn','Unknown')

    # standardize the Scooter name for each vehicule type
    df= df.replace('Scoot', 'Scooter')




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



