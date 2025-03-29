# Contando itens na lista
#Crie uma lista chamada compras com os seguintes itens:
compras = ["banana", "maçã", "banana", "laranja", "banana", "pera", "maçã"]
#Agora, faça:

#Conte quantas vezes "banana" aparece na lista usando .count().
print(f"Bananas: {compras.count('banana')}")

#Peça ao usuário para digitar um item e veja quantas vezes ele aparece.
verifica = input("digite um item  para saber quantos tem na lista: ")
if verifica in compras:
    print(f"{verifica} aparece {compras.count(verifica)}x na lista ")