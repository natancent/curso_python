roupas = {
    "camisa": 30.99,
    "camisa premium": 59.90,
    "calça": 100.00,
    "casaco": 300.00
}

carrinho = []

while True:
    digita_roupa = input("\nDigite o nome do produto (ou 'sair' para finalizar): ").strip().lower()
    
    if digita_roupa == "sair":
        break  # Sai do loop e exibe o carrinho

    if digita_roupa in roupas:
        print(f"Temos {digita_roupa} em nossa loja")
        
        ad_carrinho = input("Deseja adicionar o produto ao carrinho? (S / N) ").strip().upper()
        
        if ad_carrinho == "S":
            try:
                qtde = int(input("Qual a quantidade? ").strip())
                if qtde > 0:
                    preco_total = qtde * roupas[digita_roupa]
                    
                    carrinho.append({"produto": digita_roupa, "quantidade": qtde, "preço total": preco_total})
                    
                    continua = input("Deseja continuar comprando? (S / N) ").strip().upper()
                    if continua != "S":
                        break  # Sai do loop e exibe o carrinho
                
                else:
                    print("Erro: a quantidade deve ser maior que zero.")
            except ValueError:
                print("Erro: digite um número válido para a quantidade.")    
    else:
        print("Produto não encontrado. Tente novamente.")

# Exibir o carrinho de compras
if carrinho:
    print("\nSeu carrinho de compras:")
    total_compra = 0  
    
    for item in carrinho:
        print(f"{item['quantidade']}x {item['produto']} - R${item['preço total']:.2f}")
        total_compra += item['preço total']
    
    print(f"\nTotal da compra: R${total_compra:.2f}")
else:
    print("\nVocê não adicionou nenhum produto ao carrinho.")

        
                
                    
                    
            
            
        