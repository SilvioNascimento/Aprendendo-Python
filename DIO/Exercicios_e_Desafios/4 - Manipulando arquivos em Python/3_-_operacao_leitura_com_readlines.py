file = open('lorem.txt', 'r')

# iterando cada elemento string da lista criada pelo readline
for line in file.readlines():
    print(line)

file.close()

file2 = open('lorem.txt', 'r')

print(file2.readlines())

file2.close()
