# Intro
Get the data of boroughs from Wikipedia

# Install
```
import requests
import pandas as pd

from bs4 import BeautifulSoup

import numpy as np
import json
!conda install -c conda-forge geopy --yes
from geopy.geocoders import Nominatim
from pandas.io.json import json_normalize
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
import folium
%pip install geocoder
import geocoder
```

- Use the URL of Wikipedia to import dataframe dataset into Jupyter
```
URL = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
url = requests.get(URL)
soup = BeautifulSoup(url.content, "lxml") 

table = soup.find_all('table')[0] 
df = pd.read_html(str(table))[0]
```
First 5 rows of the imported dataframe

![](images/1.df.head().png)

