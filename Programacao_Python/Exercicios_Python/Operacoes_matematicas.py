# Escreva um programa que receba dois números e um sinal
# e faça a operação matemática definida pelo sinal

n1 = int(input("Type the first number: "))
sinal = input("Type the signal: ")
n2 = int(input("Type the second number: "))

if sinal == "+":
    op = n1 + n2
elif sinal == "-":
     print("op =", n1 - n2)
elif sinal == "*":
    print("op =", n1 * n2)
elif sinal == "/":
    print("op =",  n1 / n2)

else:
    print("Invalid signal")