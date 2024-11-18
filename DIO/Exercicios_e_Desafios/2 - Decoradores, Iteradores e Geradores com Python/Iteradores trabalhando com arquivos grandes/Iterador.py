class FileIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r', encoding='utf-8')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line != "":
            return line.strip()

        else:
            self.file.close()
            raise StopIteration


# Uso do FileIterator
for lines in FileIterator('texto.txt'):
    print(lines)
