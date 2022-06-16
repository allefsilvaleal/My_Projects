# Pega uma funcao e aplica a todos elementos de uma lista

def dobro(x):
    return x*2

valor = int(input("Digite o valor: "))

print(dobro(valor))

print("Exemplo 2")

def dobro(x):
    return x**2
valor = [1,2,3,4,5]
valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)