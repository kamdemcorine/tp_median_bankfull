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
