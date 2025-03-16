#Cálculo de Área de um triângulo

base = round(float(input("Digite a base: ")))
altura = round(float(input("Digite a altura: ")))
area = (int(base) * int(altura)) / 2 
perimettro = (int(base) + int(altura) + int(area))
print("Área: ", area)
print("Perímetro: ", perimettro)  

