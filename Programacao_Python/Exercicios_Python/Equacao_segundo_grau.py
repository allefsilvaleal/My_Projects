# Exercicio 3

# Escreva um programa que resolva uma equação de segundo grau
# Equacao de segundo grau = ax**2 + b*x + c
# Delta = b**2-4*a*c
# X = (-b+/-delta**0.5)/(2*a)


from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
 
if delta < 0:
    print("Delta negativo")
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)
