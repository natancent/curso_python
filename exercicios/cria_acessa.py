
frutas = {
    "banana":  4.00,
    "uva":     3.00, 
    "morango": 5.99,
    "laranja": 2.99,
    "abacate": 4.49
}
pedidos_compra = []
carrinho =[]

checkout = True
while checkout == True:
    fruta_digitada = input("Digite a fruta pra procurar na lista: ").lower().strip()
    
    if fruta_digitada in frutas:
        print(f"Temos {fruta_digitada.upper()}  na nossa lista!")
        ad_carrinho = input("Deseja adicionar ao carrinho? (S / N): ").strip().upper()
        if ad_carrinho == "S":
            carrinho.append((fruta_digitada.upper(), frutas[fruta_digitada]))
            print(f"{fruta_digitada.upper()} adicionada ao carrinho")
            conta = input("Deseja continuar as compras? (S / N)").strip().upper()
            if conta == "S":
                checkout = True
                continue
            else:
                break 
        else:
            continue
    else:
        print(f"Não temos {fruta_digitada.upper()} em nossa lista")
        pedido = input("Deseja incluir na lista de compras? (S / N): ").strip().upper()
        if pedido == "S":
            pedidos_compra.append(fruta_digitada)
            print(f"{fruta_digitada.upper()} adicionada á nossa lista de compras")
        else:    
            continue
total = sum(preco for _, preco in carrinho)
         
print(f"Seus pedidos:\n {carrinho}")
