import json
import pandas as pd

with open("yelp_academic_dataset_review.json", encoding="utf8") as f:
    data = json.load(f)[:30000]

review_df = pd.DataFrame(data)

# Nos quedamos solo con las reseñas que marcan 1 o 5 estrellas para conseguir mejores resultados en el entrenamiento.
review_df = review_df[(review_df['stars'] == 1) | (review_df['stars'] == 2) | (review_df['stars'] == 5) ]

# Se reemplazan los valores en la columna stars de 1 a 0 y 5 a 1 para entrenar el modelo
review_df['liked'] = review_df['stars'].replace({1:0, 2:0, 5:1})

# Filtramos solo para quedarnos solo con el texto de la reseña y la estrella
review_df = review_df[['text', 'liked']]

print("Reviews for training:",len(review_df))
print(review_df.head())