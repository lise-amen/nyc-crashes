
#NOT FONCTIONNAL 


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
