'''
faturamento = float(input("Digite o faturamento da empresa: "))
custo = float(input("Digite o custo da empresa: "))
novas_vendas = float(input("Digite o número de novas vendas: "))
aluguel = float(input("Digite o valor do aluguel: "))
salarios = float(input("Digite o valor dos salários: "))
impostos = float(0.1 * faturamento) 
 
restituicao= impostos + 0.1
lucro = faturamento - custo - aluguel - salarios - impostos + restituicao
print("O lucro da empresa é de R$", lucro)

print("A restituição foi de :" , restituicao)

#Transformar ttempo em meses em anos
tempo_meses = int(input("Digite o tempo em meses: "))
tempo_anos = int (tempo_meses / 12)    #divisão inteira
tempo_meses = tempo_meses % 12        #resto da divisão
print(f"O tempo em é de {tempo_anos} anos {tempo_meses} e meses")
'''
aluno1 = float(input("Digite a nota do aluno 1: "))
aluno2 = float(input("Digite a nota do aluno 2: "))

media = (aluno1 + aluno2) / 2
print("A média do aluno é de: ", media)





    
