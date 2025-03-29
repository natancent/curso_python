extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")



while True:
        try:
            entrada = int(input("Digite seu número: "))    
            
            if 0 <= entrada <= len(extenso):  ### ESTUDAR MAIS

                print(extenso[entrada].upper()) ### ESTUDAR MAIS
                
            else:    
                
                print("Número inválido ,tente novamente") 

            
            sair = input("Digite 'S' para SAIR ou 'C' para CONTINUAR: ").upper().strip()
            if sair == "S":
                print("Até logo!")    
                break
            if sair == "C":
                continue
                          
        except ValueError:
            print("Digite somente números!") 
            continue   
            
    
     