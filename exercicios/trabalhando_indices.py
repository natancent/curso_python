#Trabalhando com índices
#Dada a lista de números:
numeros = [10, 20, 30, 40, 50, 60]

#Exiba o terceiro elemento da lista.
print("O TERCEIRO número/elemento da lista é:",numeros[2])
#Mostre o último número usando índices negativos.
print("O ÚLTIMO número/elemento da lista é:",numeros[-1])


#Inverta a lista e exiba o resultado.
numeros.sort(reverse = True)
print(numeros)

# Desafio extra: Some todos os valores da lista usando sum().
contagem = sum(numeros)
print(contagem)