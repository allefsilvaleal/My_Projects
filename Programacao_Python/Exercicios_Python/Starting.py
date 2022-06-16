# Criando arquivo TXT
with open("arquivo.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("Eu sou um bolinho de arroz\n")
    arquivo.write("Eu sou fat\n")

# Lendo arquivo TXT
with open("arquivo.txt", "r", encoding = "utf-8") as arquivo:
    print(arquivo.read(), end = "")