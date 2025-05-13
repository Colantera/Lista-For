for numero in range(1,101):
    if numero % 2 == 0:
        print(numero)

# ou

pares = 0
for i in range(1,101):
    if i % 2 == 0:
        pares += 1
print()
print(f"Existe: {pares} pares")