import streamlit as st          # importa a biblioteca que transforma scripts de dados para aplicativos da web
import pandas as pd             # importa a biblioteca que trabalha com manipulação e análises de dados
import plotly.express as px     # importa a biblioteca que trabalha com gráficos


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

# Cria um gráfico do tipo barra de 'df_books' da coluna 'year of publication'
fig = px.bar(df_books["year of publication"].value_counts())

# Cria um gráfico do tipo histograma de 'df_books' da coluna 'book price'
fig2 = px.histogram(df_books["book price"])

# Exibe os gráficos criados um ao lado do outro
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
