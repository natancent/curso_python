##numero_int = 50 #Variável do tipo numero inteiro
##numero_float = 2.5 #Variável do tipo numero float
##texto = "Natan Vicente" #Varável do tipo String
##logica = True #Variável do tipo lógica boolean
##
##print(type(numero_int))
##print(type(numero_float))
##print(type(texto))
##print(type(logica))

# Exercício 1: Tipos de Dados e Print
# Crie variáveis de diferentes tipos (int, float, string, bool) e imprima seus valores e tipos.
nome = input("Favor digite o seu nome: ")
idade = 37
altura = 1.66
male = True
salario = 2000

print(nome)
print(type(nome))

print(idade)
print(type(idade))

print(altura)
print(type(altura))

print(male)
print(type(male))

print(salario)
print(type(salario))

# Exercício 2: Conversão de Tipos
# Converta um número para string e vice-versa, depois exiba os resultados.
new_salario = int(salario)
new_idade = str(idade)

print(new_idade,new_salario)
print(type(new_idade))
print(type(new_salario))
 
 #Exercício 3: Operações com Variáveis
 #Peça para o usuário inserir dois números, some-os e mostre o resultado.
sal_jan = int(input("Insira o salário de Janeiro:"))
sal_fev = int(input("Insira o salário de Fevereiro:"))
sal_mar = int(input("Insira o salário de Março:"))

soma_sal = sal_jan + sal_fev + sal_mar
poupa = soma_sal * 0.1 
porcent = (poupa / soma_sal) * 100
valor_poupado = soma_sal - poupa 
print(f"Você recebeu R${soma_sal:.2f} em 3 meses")
print(f"Você poupou R${poupa:.2f} ({porcent:.0f}% dos ganhos totais nesse periodo) ")
 
#Exercício 4: Manipulação de Strings
#Peça ao usuário para digitar um nome e exiba a quantidade de caracteres e o nome em maiúsculas.
number_letter = len(nome)
upper = nome.upper()

print(number_letter)
print(upper)



# Exercício 5: Booleanos e Condições
# Peça ao usuário para inserir um número e verifique se ele é positivo, negativo ou zero.

numero = int(input("favor digite um número:"))

if numero > 0:
    print(f"Número {numero} é Positivo")
elif numero < 0:
    print(f"Número {numero} é Negativo")
else:
    print("Número igual a Zero")
 










