#Ordenando e removendo itens
#Crie uma lista chamada notas com os seguintes valores:
notas = [8.5, 7.2, 9.0, 5.5, 6.8, 10.0, 4.0]
#Agora, faça:
#Ordene a lista do menor para o maior e exiba o resultado.
notas.sort()
print(notas)

#Remova a menor nota da lista.
notas.pop(0)
print(notas)


#Exiba a maior nota usando max().
notas = max(notas)
print(notas)
## Desafio extra: Calcule a média das notas e exiba se o aluno foi aprovado (média ≥ 6) ou reprovado.
#
notas = []
notas.append(float(input("Nota Matemática: ")))
notas.append(float(input("Nota História: ")))
notas.append(float(input("Nota Geografia: ")))
notas.append(float(input("Nota Português: ")))

soma = sum(notas)
quantidade = len(notas)

media = soma / quantidade

if media >= 6:
    print(f"Média final foi {media:.1f} e você foi APROVADO!")
else:
    print(f"Média final foi {media:.1f} e você foi REPROVADO!")    




