comprou_aqui = int(input("Quantas vezes cliente já comprou na loja?"))
vitrine = {
    "Casaco": 200.00,
    "Calça Jeans": 150.00,
    "Tênis": 300.00,
    "Camiseta": 150.00
} 

compra = ["Camiseta","Tênis","Casaco","Casaco"]


total = sum(vitrine[item] for item in compra if item  in vitrine  )
desconto = total * 0.10

if total > 500 or comprou_aqui >= 3:
    preco_desconto = total - desconto
    print(f"Sua compra deu R${total:.2f}\nVocê teve desconto de R${desconto:.2f} e paga R${preco_desconto:.2f}")
else:
    print(f"O valor de sua compra é: R${total:.2f}")