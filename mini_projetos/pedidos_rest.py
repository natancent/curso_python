precos =  {
    "Cerveja": 8.00,
    "Caipirinha": 15.00,
    "Refrigerante": 5.00,
    "Negroni": 15.00,
    "Croquete": 23.00,
    "Steak": 35.00,
    "Fish": 40.00,
    "Estacionamento": 5.00,
    "Entrada": 50.00,
    "Guarda - Volumes": 20.00
}


pedidos = [
    *["Cerveja"] * 2, "Caipirinha",*["Negroni"] * 2 ,"Croquete", "Fish", 
    "Estacionamento", "Entrada", "Entrada", *["Guarda - Volumes"]* 6
]

subtotal = sum(precos[item] for item in pedidos if item in precos) 
taxa = subtotal * 0.10
total = subtotal + taxa
print(f"Nome Fictício do Restaurante: Sabor da Terra\nCNPJ Fictício: 12.345.678/0001-90\nSubtotal  R${subtotal:.2f}\nTaxa de serviço(10%)  R${taxa:.2f}\nTotal  R${total:.2f}")
