# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import jalon3_baccouche_houssemipynb as module



# categories_count = ['1', '2', '3']
# chosen_count = st.selectbox(
#     'Choisir le nombre de topic !',
#     categories_count
# )

text_value= st.text_input("Entrez un texte:")
number = st.number_input('Insert a number of topics',min_value=1,max_value=15,step=1)
#st.write('The current number is ', number)
genre = st.sidebar.radio(
    "Quel Texte Analyser ?",
    ('Avis dataset', 'Texte Libre'))

if genre == 'Avis dataset':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

if st.button("Detecter le sujet d'insatisfaction"):
    p,l=module.prediction_text(module.vectorizer, module.nmf_model, number, text_value)
    st.write('Polarity is:',p)
    st.write('Topics are :',l)