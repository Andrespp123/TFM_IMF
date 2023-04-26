import pickle
import requests
import pandas as pd

# Cargamos el modelo entrenado
with open('modelo_entrenado_v1.pkl', 'rb') as f:
    model = pickle.load(f)

# Usamos el modelo en nuestro código para comprobar que funciona
# prediction = model.predict()

# Llave privada de YELP API
API_KEY = 'ZCiemO3dscUrsLb8INf1d3KaA6hZPEkhbmvCu6va162wz4c2G-04aiCGEux729ZetfonkA41i68V2AIsFMxhXR68sa0xteZQRmot_J8KhRjvU_KFRxVxurlgOuJGZHYx'

# Configuramos los parámetros para realizar el request del API
url = 'https://api.yelp.com/v3/businesses/{restaurant_id}/reviews'
headers = {'Authorization': f'Bearer {API_KEY}' }
params = {'sort_by': 'desc'}

# Hacemos el request al API 
response = requests.get(url.format(restaurant_id='YOUR_RESTAURANT_ID_HERE'), headers=headers, params=params)
reviews = response.json()['reviews']