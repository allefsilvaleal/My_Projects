print("Apresentarei tres formas de list comprehension \n")

print("Forma 1 \n")
x = [1,2,3,4,5]
y = []
for i in x:
    y.append(i ** 2)
print(x)
print(y)

print("\n")
print("Forma 2 \n")
x = [1,2,3,4,5]
y = [i ** 2 for i in x]
print(x)
print(y)

print("\n")
print("Forma 3 \n")
x = [1,2,3,4,5]
y = [i ** 2 for i in x]
z = [i for i in x if i % 2 == 1]
print(x)
print(y)
print (z)