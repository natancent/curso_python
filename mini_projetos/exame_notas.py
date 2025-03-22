nota01 = float(input("Digite a nota 1: "))
nota02 = float(input("Digite a nota 2: "))
nota03 = float(input("Digite a nota 3: "))

media = (nota01 + nota02 + nota03) / 3
print(f"Média: {media:.1f}")

# Verifica se a média é maior ou igual a 7 e se todas as notas são >= 5
if media >= 7 and nota01 >= 5 and nota02 >= 5 and nota03 >= 5:
    print("Você passou!")
else:
    print("Você reprovou!")
