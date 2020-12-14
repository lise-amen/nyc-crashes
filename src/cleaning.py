import numpy as np
import pandas as pd

def exploring_data(df) : 
    print(df.info()) # Index, Datatype and Memory information
    missing_values_count = df.isnull().sum()
    print(missing_values_count) #number missing values

def clean_data(df) :
    df = df.drop_duplicates(subset=None, keep='first', inplace=False) #drop duplicate data 
    df = df[df['location'].notna()] #drop location without information
    
    # replace nan values in the dataset by 'Unspecified' in contributing_factor_vehicule columns 
    df[['contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4', 'contributing_factor_vehicle_5']] = df[['contributing_factor_vehicle_1','contributing_factor_vehicle_2', 'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4', 'contributing_factor_vehicle_5']].fillna('Unspecified')

    return df 

def rename_column(df) :

    #rename column to standardizer
    df = df.rename(columns={'vehicle_type_code2':'vehicle_type_code_2'})
    df = df.rename(columns={'vehicle_type_code1':'vehicle_type_code_1'})

    return df 
    
    
def clean_string_vehicle(df) : 

    # capitalize the first character of each word for vehicule type 
    df = df.str.title()

    # standardize the ambulance name for each vehicule type
    df = df.replace('Ambul', 'Ambulance')
    df = df.replace('Ambu', 'Ambulance')
    df = df.replace('Ambulace', 'Ambulance')
    df = df.replace('Amb', 'Ambulance')
    df = df.replace('Ambu', 'Ambulance')
    df = df.replace('Ambulence', 'Ambulance')
    df = df.replace('Almbulance', 'Ambulance')
    df = df.replace('White Ambu', 'Ambulance')

    # standardize the Fire Truck name for each vehicule type
    df = df.replace('4 Dr Sedan', 'Sedan')
    df = df.replace('2 Dr Sedan', 'Sedan')

    # rename E-Sco by E-Scooter
    df = df.replace('E-Sco', 'E-Scooter')

    # rename E-Bike by E-Bik
    df = df.replace('E-Bik', 'E-Bike')
    df = df.replace('E Bike', 'E-Bike')

    # standardize the Fire Truck name for each vehicule type
    df= df.replace('Fire', 'Fire Truck')

    # standardize the Unknow name for each vehicule type
    df = df.replace('Unk', 'Unknown')
    df = df.replace('Unkno', 'Unknown')
    df = df.replace('Unkno', 'Unknown')
    df = df.replace('0', 'Unknown')
    df = df.replace('Unkn','Unknown')

    # standardize the Scooter name for each vehicule type
    df = df.replace('Scoot', 'Scooter')

    return df 



