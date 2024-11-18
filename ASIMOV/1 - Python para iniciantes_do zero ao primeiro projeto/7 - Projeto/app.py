import streamlit as st      # importa a biblioteca que transforma scripts de dados para aplicativos da web
import pandas as pd         # importa a biblioteca que trabalha com manipulação e análises de dados

# Estica a tabela de dados
st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./datasets/customer reviews.csv")
df_top100_books = pd.read_csv("./datasets/Top-100 Trending Books.csv")

# Procura o maior preço dos livros top 100
price_max = df_top100_books["book price"].max()

# Procura o menor preço dos livros top 100
price_min = df_top100_books["book price"].min()

# Adicionando um slider dentro de um sidebar de streamlit
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# Filtra os dados que será exibido na tabela pelo 'max_price'
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books
