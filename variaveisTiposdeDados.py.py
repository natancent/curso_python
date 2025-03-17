#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#altura = float(input("Digite sua altura: "))
#status = bool(input("Digite seu status: "))
#
#print(f"Seu nome é {nome}, você tem {idade} anos e {altura} de altura.")
#
#print(f"O tipo da variável nome é {type(nome)}")
#print(f"O tipo da variável idade é {type(idade)}")
#print(f"O tipo da variável altura é {type(altura)}")
#print(f"O tipo da variável status é {type(status)}")

#Desafios
#1 - Faça um programa que leia um número inteiro e o imprima.
numero = int(input("Digite um número inteiro: "))
print(f"O número digitado foi {numero}")

#2 - Faça um programa que leia um número real e o imprima.
numero = float(input("Digite um número real: "))
print(f"O número digitado foi {numero}")

#3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))
soma = numero1 + numero2 + numero3
print(f"A soma dos números digitados é {soma}")

#4 - Peça ao usuário para digitar um número e imprima o quadrado dele.
numero = int(input("Digite um número: "))
quadrado = numero ** 2
print(f"O quadrado do número digitado é {quadrado}")

#5 - Faça um programa que leia o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
salario = float(input("Digite o salário do funcionário: "))
percentual = float(input("Digite o percentual de aumento: "))
aumento = salario * percentual / 100
novoSalario = salario + aumento
print(f"O aumento foi de R${aumento:.2f} e o novo salário é R${novoSalario:.2f}")






