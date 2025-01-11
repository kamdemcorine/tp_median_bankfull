#dashboard bank-full

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import pydeck as pdk

data = pd.read_csv('bank-full.csv', delimiter = ';')
#titre du tableau de bord
st.title("Tableau de bord interactif - Bank Full dataset")

#afficher les premieres lignes du jeu de donnees
st.header('Apercu du jeu de donnees')
st.write(data.head())

#Distribution des ages
st.header('Distributuin des ages')
fig,ax = plt.subplots()
sns.histplot(data['age'], bins= 30, kde = True, ax = ax)
ax.set_title('Distributuin des ages')
ax.set_xlabel('Age')
ax.set_yabel('Frequence')
st.pyplot(fig)

# Taux de souscription en fonction du travail et du niveau d'éducation 
st.header('Taux de Souscription en Fonction du Travail et du Niveau d\'Éducation') 
fig, ax = plt.subplots(figsize=(12, 6)) 
sns.countplot(x='job', hue='education', data=data, ax=ax) 
ax.set_title('Taux de Souscription en Fonction du Travail et du Niveau d\'Éducation') 
ax.set_xlabel('Travail') 
ax.set_ylabel('Nombre de Souscriptions') 
ax.legend(title='Niveau d\'Éducation') 
st.pyplot(fig)

#Répartition des soldes bancaires 
st.header('Répartition des Soldes Bancaires') 
fig, ax = plt.subplots() 
sns.histplot(data['balance'], bins=30, kde=True, ax=ax) 
ax.set_title('Répartition des Soldes Bancaires') 
ax.set_xlabel('Solde') 
ax.set_ylabel('Fréquence') 
st.pyplot(fig)

# Durée des appels en fonction du mois 
st.header('Durée des Appels en Fonction du Mois') 
fig, ax = plt.subplots(figsize=(12, 6)) 
sns.boxplot(x='month', y='duration', data=data, ax=ax) 
ax.set_title('Durée des Appels en Fonction du Mois') 
ax.set_xlabel('Mois') 
ax.set_ylabel('Durée (secondes)') 
st.pyplot(fig)
