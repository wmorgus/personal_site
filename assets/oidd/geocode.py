import geocoder
import pandas as pd
import csv

def do_geocode_lat(x):
  try:
    g = geocoder.geonames(x, key='wmorgus')
    print(dir(g))
    print(g.status)
    if (g.status == "OK"):
      print('good')
      print(x)
    else:
      print('no good')
      print(x)
    return str(geocoder.geonames(x).latlng[0])
  except Exception as e: 
    # print(e)
    return 'null'

def do_geocode_long(x):
  try:
    g = geocoder.geonames(x)
    # print(dir(g))
    return str(g.latlng[1])
  except:
    return 'null'

df = pd.read_csv('tripadvisor.csv')
print(df.head(20))
discardRows = []
for index, row in df.iterrows():
  nullFlag = False
  for item in row:
    try:
      if 'null' in item:
        discardRows.append(index)
    except:
      pass

df.drop(discardRows)

df["address"] = df["address"].apply(lambda x: str(x) + ', Philadelphia, PA')
df["latitude"] = df["address"].apply(lambda x: do_geocode_lat(x))
df["longitude"] = df["address"].apply(lambda x: do_geocode_long(x))
df.dropna()

df.to_csv('clean_tripadvisor.csv', index=False)