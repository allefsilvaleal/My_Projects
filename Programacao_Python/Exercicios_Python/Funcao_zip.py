# Zip vai compactar duas listas como se fosse uma única lista

lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "casa", "dinheiro", "elefante"]
lista3 = ["fruta", "objeto", "imovel", "objeto", "animal"]

for numero, nome, outros in zip(lista1, lista2, lista3):
    print(numero, nome, outros)