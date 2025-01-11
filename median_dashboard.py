#dashboard bank-full

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

data = pd.read_csv('bank-full.csv', delimiter = ';')
#titre du tableau de bord
st.title("Tableau de bord interactif - Bank Full dataset")

#afficher les premieres lignes du jeu de donnees
st.header('Apercu du jeu de donnees')
st.write(data.head())

# Distribution des âges 
st.header('Distribution des Âges') 
age_hist = alt.Chart(data).mark_bar().encode( 
  alt.X('age:Q', bin=alt.Bin(maxbins=30)), 
  y='count()', 
  tooltip=['age', 'count()'] ).properties( 
  title='Distribution des Âges' ) 
st.altair_chart(age_hist, use_container_width=True)

# Taux de souscription en fonction du travail et du niveau d'éducation 
st.header('Taux de Souscription en Fonction du Travail et du Niveau d\'Éducation') 
job_education_chart = alt.Chart(data).mark_bar().encode( 
  x='job:N', 
  y='count()', 
  color='education:N', 
  tooltip=['job', 'education', 'count()'] ).properties( 
  title='Taux de Souscription en Fonction du Travail et du Niveau d\'Éducation' ).interactive() 
st.altair_chart(job_education_chart, use_container_width=True)

#Répartition des soldes bancaires 
st.header('Répartition des Soldes Bancaires') 
balance_hist = alt.Chart(data).mark_bar().encode( 
  alt.X('balance:Q', bin=alt.Bin(maxbins=30)), 
  y='count()', tooltip=['balance', 'count()'] ).properties( 
  title='Répartition des Soldes Bancaires' ) 
st.altair_chart(balance_hist, use_container_width=True)

# Durée des appels en fonction du mois 
st.header('Durée des Appels en Fonction du Mois') 
duration_month_boxplot = alt.Chart(data).mark_boxplot().encode( 
  x='month:N', 
  y='duration:Q', tooltip=['month', 'duration'] ).properties( 
  title='Durée des Appels en Fonction du Mois' ) 
st.altair_chart(duration_month_boxplot, use_container_width=True)


import streamlit as st
import pandas as pd
import altair as alt
import joblib
from sklearn.ensemble import RandomForestClassifier

# Charger le modèle pré-entraîné
model = joblib.load('random_forest_model.pkl')

# Simulation des prédictions
st.header('Simulation des Prédictions')
st.write('Entrez les caractéristiques pour prédire la souscription :')

# Créer des champs de saisie pour les caractéristiques
age = st.number_input('Âge', min_value=18, max_value=100, value=30)
job = st.selectbox('Travail', data['job'].unique())
marital = st.selectbox('État civil', data['marital'].unique())
education = st.selectbox('Niveau d\'éducation', data['education'].unique())
default = st.selectbox('Défaut de crédit', ['yes', 'no'])
balance = st.number_input('Solde', value=1000)
housing = st.selectbox('Prêt immobilier', ['yes', 'no'])
loan = st.selectbox('Prêt personnel', ['yes', 'no'])
day = st.number_input('Jour de contact', min_value=1, max_value=31, value=15)
month = st.selectbox('Mois de contact', data['month'].unique())
duration = st.number_input('Durée de l\'appel (secondes)', value=300)
campaign = st.number_input('Nombre de contacts pendant cette campagne', value=1)
pdays = st.number_input('Nombre de jours depuis le dernier contact', value=-1)
previous = st.number_input('Nombre de contacts avant cette campagne', value=0)

# Créer un DataFrame avec les caractéristiques saisies
input_data = pd.DataFrame({ 
  'age': [age], 
  'job': [job], 
  'marital': [marital], 
  'education': [education], 
  'default': [default], 
  'balance': [balance], 
  'housing': [housing], 
  'loan': [loan], 
  'day': [day], 
  'month': [month], 
  'duration': [duration], 
  'campaign': [campaign], 
  'pdays': [pdays], 
  'previous': [previous] })

# Prédire la souscription 
if st.button('Prédire'): 
  prediction = model.predict(input_data) 
  st.write(f'Prédiction : {"Souscription" if prediction[0] == "yes" else "Pas de souscription"}')



