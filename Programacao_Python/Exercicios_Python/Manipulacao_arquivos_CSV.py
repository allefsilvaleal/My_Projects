# import csv

# with open("caso_full.csv", "r", encoding = "utf-8") as arquivo_csv:
  #  leitor = csv.reader(arquivo_csv)
   # for linha in leitor:
    #    print(linha)

# import csv

#with open("users.csv", "w", encoding = "utf-8", newline = "") as arquivo_users:
 #   escritor = csv.writer(arquivo_users)
  #  escritor.writerow(["Nome", "Sobrenome", "E-mail", "Genero"])
   # escritor.writerow(["Allef", "Leal", "allefsilvaleal@hotmail.com", "Masculino"])

import csv

header = ["Nome", "Sobrenome"]
dados = []
opt = (input("O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n "))

while opt == "1":
        Nome = (input("Qual seu nome? ")).capitalize()
        Sobrenome = (input("Qual seu sobrenome? ")).capitalize()
        dados.append([Nome, Sobrenome])
        opt = (input("\nO que deseja fazer?\n1 - Cadastrar\n0 - Sair\n "))

"""    elif opt == "0":
        Nome = (input("Qual seu nome? ")).capitalize()
        Sobrenome = (input("Qual seu sobrenome? ")).capitalize()
        dados.append([Nome, Sobrenome])
        opt = (input("\nO que deseja fazer?\n1 - Cadastrar\n0 - Sair\n "))
    else:
        while opt != "0" or "1":
            print("Tente novamente")
            opt = (input("\nO que deseja fazer?\n1 - Cadastrar\n0 - Sair\n "))"""

print(dados)

with open("user_2.csv", "w", newline = "") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerow(dados)

with open("user_2.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)