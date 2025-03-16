valor_produto = float(input("Digite o valor do produto: "))
desconto = valor_produto * 0.05
valor_produto = valor_produto - desconto
print("O valor do produto com desconto é: {:.2f}".format(valor_produto))
print("O desconto foi de: {:.2f}".format(desconto))

