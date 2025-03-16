#nome = input("Digite o seu nome completo: ") #Recebe o nome completo
#Extrai primeiro nome
#primeiro_nome = nome.split()[0] #Separa o nome completo em uma lista e pega o primeiro elemento
#letra_maiuscula = primeiro_nome.capitalize() #Coloca a primeira letra do nome em maiúscula
#print("Olá {}, seja bem vindo ao nosso sistema!".format(letra_maiuscula)) #Imprime a saudação com o nome em maiúscula

email = input("Digite o seu e-mail: ") 

usuario , dominio = email.split("@",1) 

print("Usuário {} cadastrado com sucesso!".format(usuario)) 

prim_letra = usuario[0]
seg_letra = usuario[1] if len(usuario) > 1 else ""
ult_letra = usuario[-1] if len(usuario) > 2 else ""

if len(usuario) > 2: 
    email_escondido = prim_letra + seg_letra +  "*"*(len(usuario)-3) + ult_letra + "@" + dominio 
else: 
    email_escondido = prim_letra + "*" * (len(usuario)-1)+ "@" + dominio  

print("Um link foi enviado para {}".format(email_escondido )) #Imprime o e-mail escondido




