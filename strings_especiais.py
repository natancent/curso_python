faturamento = 1500
custo = 400
novas_vendas = 1000
lucro = faturamento - custo + novas_vendas
margem_lucro = (lucro / faturamento) * 100 

#exibir lucro com 2 casas decimais 
#print("O lucro foi de: R${:.2f}".format(lucro))

#trocar o ponto por vírgula
#print("O lucro foi de: R${:.2f}".format(lucro).replace(".", ","))

#exibir margem de lucro com 2 casas decimais e com %
#print("A margem de lucro foi de: {:.0f}%".format(margem_lucro))

# Exibir informações com quebra de linha \n
print("O lucro foi de: R${:.2f}\n Os custos foram de R${:.2f}\n As novas vendas foram de {:.2f}\n O lucroA margem de lucro foi de: {:.0f}%".format(lucro,custo,novas_vendas, margem_lucro).replace(".", ","))







