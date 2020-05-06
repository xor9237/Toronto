import urllib.request, json
import requests
import pandas as pd
from bs4 import BeautifulSoup

import numpy as np
import json

from geopy.geocoders import Nominatim
from pandas.io.json import json_normalize
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
import folium

import geocoder

# Scrape from URL
URL = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
url = requests.get(URL)
soup = BeautifulSoup(url.content, "lxml")

table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]

# drop rows with 'Not assigned' in Borough column
df = df[df.Borough != 'Not assigned'].reset_index()

#to check the size of the data frame
print(df.shape)

# Replace "/" to "," in the column Neighborhood
df['Neighborhood'] = df['Neighborhood'].str.replace("/", ",")

