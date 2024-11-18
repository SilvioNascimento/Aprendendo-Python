import streamlit as st      # importa a biblioteca que transforma scripts de dados para aplicativos da web
import pandas as pd         # importa a biblioteca que trabalha com manipulação e análises de dados

# Estica a tabela de dados
st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./datasets/customer reviews.csv")
df_top100_books = pd.read_csv("./datasets/Top-100 Trending Books.csv")






