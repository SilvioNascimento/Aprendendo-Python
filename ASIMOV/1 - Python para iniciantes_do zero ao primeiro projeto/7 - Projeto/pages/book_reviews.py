# Este código aparecerá como uma nova página a ser acessada na web quando o projeto for executado

import streamlit as st      # importa a biblioteca que transforma scripts de dados para aplicativos da web
import pandas as pd


# Estica a tabela de dados
st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./datasets/customer reviews.csv")
df_top100_books = pd.read_csv("./datasets/Top-100 Trending Books.csv")

# Pega apenas os títulos de cada livro sem repetição
books = df_top100_books["book title"].unique()

# Criar um select box de títulos de livros dentro do sidebar
book = st.sidebar.selectbox("Books", books)

# Mostra os dados de um livro selecionado no select box
df_book = df_top100_books[df_top100_books["book title"] == book]

book_title = df_book["book title"].iloc[0]                  # Pegando o título do livro
book_genre = df_book["genre"].iloc[0]                       # Pegando o gênero do livro
book_price = f"${df_book['book price'].iloc[0]}"            # Pegando o preço do livro
book_rating = df_book["rating"].iloc[0]                     # Pegando a avaliação do livro
book_year = df_book["year of publication"].iloc[0]          # Pegando o ano de publicação do livro

st.title(book_title)                            # Exibindo o título do livro
st.subheader(book_genre)                        # Exibindo os gêneros do livro
col1, col2, col3 = st.columns(3)                # Cria três colunas em uma linha
col1.metric("Price", book_price)                # Exibe o preço do livro
col2.metric("Rating", book_rating)              # Exibe a avaliação do livro
col3.metric("Year of publication", book_year)   # Exibe o ano de publicação do livro

st.divider()

# Mostra os dados de reviews de um livro selecionado no select box
df_reviews_f = df_reviews[df_reviews["book name"] == book]
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
