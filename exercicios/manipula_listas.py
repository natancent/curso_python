#Manipulação de listas - Adicionando e removendo itens
#Crie uma lista chamada times_futebol com 4 times que você gosta. Depois:
times_futebol = ["zion tigers","atletico","fluminense","maringa","real madrid","ponte preta","penarol"]
#Adicione mais dois times usando append().
times_futebol.append(input("Adicione um time: "))
times_futebol.append(input("Adicione outro time: "))

#Remova o segundo time usando pop().
times_futebol.pop(1)


#Troque o último time por outro time de sua escolha.
times_futebol[-1] = input("Digite o que deseja substituir: ").lower()


# Desafio extra: Ordene a lista em ordem alfabética e exiba o resultado.
times_futebol.sort()
print(times_futebol)