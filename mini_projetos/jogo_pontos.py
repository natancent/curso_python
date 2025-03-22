pontos = 100
print(f"Você tem {pontos} pontos !")
while pontos > 0:
    escolha = input("O que deseja fazer GANHAR - PERDER - MULTIPLICAR - DIVIDIR - ou SAIR para encerrar: ").upper()
    
    if escolha == "GANHAR":
        pontos += int(input(f"Quantos pontos deseja {escolha}?"))
        print(f"Você tem {pontos} pontos!")
    elif escolha == "PERDER":
        pontos -= int(input(F"Quantos pontos  deseja {escolha}?"))
        print(f"Você tem {pontos} pontos!")
    elif escolha == "MULTIPLICAR":
        pontos *= int(input(F"Quantos pontos deseja {escolha}?")) 
        print(f"Você tem {pontos} pontos!")
    elif escolha == "DIVIDIR":
        pontos //= int(input(F"Quantos pontos deseja {escolha}?"))  
        print(f"Você tem {pontos} pontos!")
    elif escolha == "SAIR":
        print(f"Obrigado por jogar , você teminou com {pontos} pontos, até logo!")
        break
    else:
        print("Opção inválida,tente novamente!")
        continue 
    
    if pontos <=0:
        print("GAME OVER")
        break
    elif pontos >= 1000:
        print(f"JACKPOT !!!\n Você chegou á {pontos} E GANHOU O JOGO!!! ")
        break  
        
    