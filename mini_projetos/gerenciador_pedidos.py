#Desafio: Gerenciador de Pedidos de um Bar 🍹
#Você foi contratado para desenvolver um sistema simples de pedidos para um bar. O programa deve:

#Exibir um menu com pelo menos 5 bebidas e seus respectivos preços.

print("Menu de Drinks")
print(" 1 Negroni - $ 30 \n 2 Boulevardier - $ 35 \n 3 Cosmopolitan - $ 27 \n 4 Margarita - $ 29 \n 5 Iced Tea - $ 18")

bebidas = {
    1: ("Negroni", 30), 
    2: ("Boulevardier", 35),
    3: ("Cosmopolitan", 27),
    4: ("Margarita", 29),
    5: ("Iced Tea", 18),
}

algo_mais = True
total = 0


while algo_mais: 
    try:
        produto = int(input("Escolha o numero referente ao seu pedido: "))
        if produto  not in bebidas:
            print("Produto inválido, tente novamente")
            continue
        qtde = int(input("Escolha a quantidade do produto escolhido: "))
        if qtde <= 0:
            print("Escolha um número maior que zero")
            continue
        preco = bebidas[produto][1]
        total += preco * qtde
        
        
        mais = input("Deseja pedir algo mais? (S ou N)").strip().upper()
        if mais != "S":
            algo_mais = False
    except ValueError:
        print("Entrada inválida , digite apenas números!")
print(f"O total de seu pedido é $ {total:.2f}")        
            
        

     


    





