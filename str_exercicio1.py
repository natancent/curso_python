# Description: Este programa recebe um email e retorna o servidor de email
nome = "Natanael Vicente Pereira" #Nome do usuário
email = "natancent1@outlook.com" #Email do usuário
localiza_arroba = email.find("@") #Localiza o arroba no email
localiza_ponto = email.find(".") #Localiza o ponto no email
servidor_email = email[localiza_arroba+1:localiza_ponto] #Retorna o servidor de email(do +1 ao ponto)
uppercase = servidor_email.upper() #Retorna o servidor de email em maiúsculo
print("O servidor de email é: {}".format(uppercase)) #Imprime o servidor de email em maiúsculo
# End
