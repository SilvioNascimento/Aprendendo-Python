arquivo = open('teste.txt', 'w')
arquivo.write('Escrevendo dados em um novo arquivo!')
arquivo.writelines(["\n", "Escrevendo", "\n", "alguma", "\n", "coisa"])
arquivo.close()
