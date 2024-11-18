arquivo = open('lorem.txt', 'r')

# linha := arquivo.readline()
#   linha -> denominando a variável 'linha' como volátil (temporário)
#   := -> ao lado esquerdo deste sinal será uma variável volátil, enquanto o lado direito será
#         um valor que a variável volátil irá armazenar

while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
