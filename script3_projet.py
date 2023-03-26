import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
from faker import Faker
import re
import requests
import bonus1

import matplotlib



client = MongoClient()
db = client['Rakuten']
promos = db['Promos']
results = promos.find().limit(100)
df = pd.DataFrame(list(promos.find()))
df["category"] = df["category"].replace("COUP DE", "COUP DE COEUR")

def extract_price(price_str):
    # Utiliser une expression régulière pour extraire les nombres
    match = re.search(r'\d+(\.\d+)?', price_str)
    if match:
        # Convertir le nombre en float
        return float(match.group())
    else:
        return None
categories = ["all"] + list(df["category"].unique())
category_filter = st.sidebar.selectbox(
    "Sélectionner une catégorie",categories)
# Appliquer la fonction extract_price au dataframe
df["price"] = df["price"].apply(extract_price)
# Créer un filtre pour la colonne 'price'
price_filter = st.sidebar.slider(
    "Sélectionner une fourchette de prix",
    float(df["price"].min()), float(df["price"].max()), (float(df["price"].min()), float(df["price"].max()))
)

# Appliquer les filtres au dataframe
if category_filter != 'all':
    df = df[
        (df["category"] == category_filter) &
        (df["price"] >= price_filter[0]) &
        (df["price"] <= price_filter[1])
    ]
else: 
    df = df[
        (df["price"] >= price_filter[0]) &
        (df["price"] <= price_filter[1])
    ]

st.write(df)
data = df[["category", "price"]]
fig, ax = plt.subplots(figsize=(12, 8))
sns.histplot(data=df, x="price", kde=True, stat="density", ax=ax)

ax.set_title(f"Distribution des prix des produits de la catégorie")
ax.set_xlabel("Prix")
ax.set_ylabel("Densité")
st.pyplot(fig)


total_products = len(df)
most_common_category = df["category"].mode().iloc[0]
mean_price = df["price"].mean()

# Affichage des statistiques
st.write(f"Les statistiques : ")
st.write(f"Nombre total de produits : {total_products}")
st.write(f"Catégorie la plus courante : {most_common_category}")
st.write(f"Prix moyen des produits : {mean_price:.2f} €")


sns.catplot(x="category", y="price", data=df, kind="box")
st.pyplot()

# recherche
search_query = st.sidebar.text_input("Rechercher des produits par titre ou description")
if search_query:
    title = df["title"]
    df = df[title.str.contains(search_query, case=False)]

st.write(df)


if st.button("Créer une nouvelle entrée"):
    bonus1.create()

if st.button("Mettre à jour une entrée"):
    bonus1.update()

if st.button("Mettre à jour une donnée"):
    bonus1.maj()

if st.button("Supprimer une entrée"):
   bonus1.delete()

st.write(df)











