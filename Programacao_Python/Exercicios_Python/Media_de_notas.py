# Faça um programa que receba duas notas digitadas pelo usuario.
# Se a nota for maior ou igual a seis e meio, escreva aprovado, senão escreva reprovado

nota_1 = float(input("Digite a nota da P1: "))
nota_2 = float(input("Digite a nota da P2:"))

media = (nota_1 + nota_2)/2

if media >= 6.5:
    print("Aprovado. Nao fara Exame ;)")
else:
    print("Reprovado. Fara exame :(")