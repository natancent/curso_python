#Exercício 1: Básico de Comparação
#Crie um programa que solicita dois números ao usuário e exibe os seguintes resultados:
#
#Se o primeiro número é maior que o segundo.
#
#Se o primeiro número é menor que o segundo.
#
#Se os números são iguais.

# ==, !=, >, <, >=, <=

#funciona = True
#while funciona == True:
#    numero1 = int(input("Favor digite um número: "))
#    numero2 = int(input("Favor digite outro número: "))
#
#
#    if numero1 == numero2:
#        print("Numeros iguais.")
#    elif numero1 > numero2:
#        print(f"Numero {numero1} é maior que {numero2}. ")
#    elif numero1 < numero2:
#        print(f"Numero {numero1} é menor que número {numero2}.")
#    elif numero1 >= numero2:
#        print(f"Numero {numero1} maior ou igual que numero {numero2}")
#    elif numero1 <= numero2:
#        print(f"Numero {numero1} menor ou igual que numero {numero2}") 
#    else:
#        print("Opção inválida ,tente novamnte!")
#        continue
#    
#    encerrar = input("Digite 'SAIR' para encerrar ou 'CONTINUE' para continuar." ).upper()
#    if encerrar == ("SAIR"):
#        print("Obrigado!")
#        funciona = False
#        break
#    elif encerrar == True:
#        continue   
    

#  🟢 Desafio 1: Jogo da Idade
#📌 Objetivo: Peça a idade do usuário e classifique em:
#
#Menor de idade (0 a 17 anos)
#
#Adulto (18 a 64 anos)
#
#Idoso (65 anos ou mais)
#
#💡 Dica: Use if, elif e else.  

#idade = int(input("Digite a idade: "))
#
#if idade < 0:
#    print("Dado inválido")
#elif idade <= 17 :
#    print("Menor")
#elif idade <=  64:
#    print("Adulto")
#else:
#    print("Idoso")                                         

# Desafio:
#O programa escolhe um número secreto (exemplo: 7).
#
#O usuário digita um número e o programa responde:
#
#Se acertou: "Parabéns! Você acertou!" 🎉
#
#Se o palpite for maior: "Muito alto! Tente um número menor."
#
#Se o palpite for menor: "Muito baixo! Tente um número maior."

numero_secreto = 7
pontos = 100


while pontos > 0:
    try: 
        palpite = int(input("Seu palpite (Digite um número): "))

        if palpite < 1 or palpite > 10:
            print("❌ Número fora do intervalo! Digite um número entre 1 e 10.")
            continue  # Volta para o início do loop sem perder pontos
        
        if palpite == numero_secreto:
            print("Parabéns , acertou!")
            break
        elif palpite < numero_secreto:
            pontos -= 10
            print(f"Muito baixo,você tem {pontos} pontos!")
        elif palpite > numero_secreto:
            pontos -= 10
            print(f"Número muito alto , você tem {pontos} pontos!")
        
    except ValueError:
        print("❌ Entrada inválida! Digite um número inteiro.")  

if pontos == 0:
    print(f"Pontos esgotaram GAME OVER!!! (número secreto era {numero_secreto})!")    

        
    
                    

