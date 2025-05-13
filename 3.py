while True:
    numero = int(input("Digite um número de 1 a 10 que queira saber a tabuada: "))
    if 1 <= numero <=10:
        break
    else:
        print("Número invalido")

print(f"Tabuado do {numero}")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")