quantidade = int(input("Você quer saber a média de quantas idade? "))
soma = 0

for i in range(quantidade):
    idade = int(input(f"Digite a idade {i + 1}: "))
    soma += idade

media = soma / quantidade
print(f"A média das idades é: {media:.2f}")