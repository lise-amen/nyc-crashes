import pandas as pd
import numpy as np
import re

from src.cleaning import *

#import dataframe
df = pd.read_csv('data/data_100000.csv')
print(df.isnull().sum())

#exploring_data(df)
df = clean_data(df)

#find any missing value for borough', 'on_street_name', 'off_street_name', 'cross_street_name on taget value location 
list = ['borough', 'on_street_name', 'off_street_name', 'cross_street_name', 'zip_code']
target = 'location'

for name in list : 
    df_out = df[[name,target]]
    df = find_datas_with_localite(df,df_out, name)


list = ['vehicle_type_code1', 'vehicle_type_code2', 'vehicle_type_code3']

#for vehicle in list :
    #df_vehicle = df[[vehicle]]
    #df = clean_string_vehicle(df_vehicle)

df.vehicle_type_code2.value_counts().to_csv('vechicule_format2')


"""
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='lise')
location = geolocator.reverse("40.829052 -73.85038")
print(location.address)


#extract zip code
df_zip = df[['zip_code','latitude','longitude']]

#keep only zip code with nan 
df_zip = df_zip[df_zip['zip_code'].isna()]

df_zip['latitude']=df_zip['latitude'].astype('string')
df_zip['longitude']=df_zip['longitude'].astype('string')

df_zip['location'] = df_zip['latitude'] + ' ' + df_zip['longitude']

print(df_zip)
"""

"""
for value in df['location']:
    geolocator = Nominatim(user_agent='lise')
    location = geolocator.reverse(value)
"""
