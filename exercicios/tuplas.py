lanche = ("burguer","pizza","risolis","kibe")
#Forma 01 
#for comida in lanche:
#  print(f"Eu vou comer {comida}")
   
#Forma 02
for cont in range(0 , len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
    
    
#Forma 03
for pos , comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos} ")
 
#Iterção de tuplas
#a = (2,4,6,8,10)
#b = (5,7,6,2,3)
#
#c = a + b
#
#print(c)
print(c.count(2))
##print(sorted(c))
#print(c.index(7))
# DADOS DE TIPOS DIFERENTES DENTRO DE TUPLAS
#
#pessoa = ("João", 37 ,"M" , 99.5)
#
#for dado in pessoa:
#    print(f"{dado}")