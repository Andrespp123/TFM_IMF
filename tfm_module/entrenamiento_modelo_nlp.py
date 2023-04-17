#!/usr/bin/env python
# coding: utf-8

# In[40]:


import nltk
import pandas as pd
import matplotlib.pyplot as plt
import pickle 
from nltk.stem import WordNetLemmatizer
from tfm_module.json_processing import review_df
from sklearn.utils import resample

plt.style.use('ggplot')

lemmatizer = WordNetLemmatizer()


# In[2]:


review_df.head()


# In[3]:


review_df.iloc[1]['text']


# In[4]:


review_df.isnull().sum()


# In[5]:


# Revisamos el dataset para posibles sesgos 
review_df['liked'].value_counts().plot(kind='bar', title='Review count', figsize=(10,5))


# In[6]:


review_df['liked'].value_counts()


# In[7]:


# Hacemos undersampling para evitar el sesgo
df_majority = review_df[review_df['liked']==1]
df_minority = review_df[review_df['liked']==0]
df_majority_undersampled = resample(df_majority, replace=False, n_samples=3226, random_state=42)
review_df = pd.concat([df_majority_undersampled, df_minority])


# In[8]:


review_df['liked'].value_counts()


# In[9]:


# Reiniciamos el índice manualmente antes del próximo paso
review_df = review_df.reset_index(drop=True)


# In[10]:


import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
ps = PorterStemmer()


reviews_procesadas=[]

for i in range(0,len(review_df)):
    text = review_df['text'][i]
    if text:
        Review = re.sub('[^a-zA-Z]',' ',review_df['text'][i])
        Review = Review.lower()
        Review = Review.split()
        Review = [ps.stem(word) for word in Review if word not in set(stopwords.words('english'))]
        Review = ' '.join(Review)
        reviews_procesadas.append(Review)
    
    else:
        reviews_procesadas.append('To discard')


# In[11]:


reviews_procesadas[0]


# In[12]:


# Sustituimos las reviews procesadas en el mismo dataframe de entrenamiento
review_df['text'] = reviews_procesadas


# In[14]:


X = review_df['text']
y = review_df['liked']


# In[15]:


# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)


# In[16]:


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)


# In[17]:


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(solver='lbfgs', random_state = 12)
clf.fit(X_train_vect,y_train)


# In[18]:


from sklearn.metrics import accuracy_score, classification_report
y_pred = clf.predict(X_test_vect)
y_pred[0:10]


# In[19]:


accuracy_score(y_test,y_pred)
print(classification_report(y_test,y_pred))


# In[33]:


test = "It is a bad but good restaurant" 

def pre_p(a):
    p = re.sub('[^a-zA-Z]',' ',a)
    p = p.lower()
    p = p.split()
    p = [ps.stem(word) for word in p if word not in set(stopwords.words('english'))]
    p = ' '.join(p)
    ejemplo = vectorizer.transform([p])
    return ejemplo.toarray()

prediction =clf.predict_proba(pre_p(test))


print(prediction[0][1])


# In[42]:


# Guardamos el modelo entrenado en un archivo

with open('modelo_entrenado_v1.pk1', 'wb') as file:
    pickle.dump(clf, file)

