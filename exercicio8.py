valorlata = int(50)
litrolata = int(5)
litro1 = int(3)

altura = int(input("digite a altura do tanque: "))
raio = int(input("digite o raio do tanque: "))
area = 2*3.14*raio*altura

quantidadelatas = area / litro1
valor = quantidadelatas*valorlata

print("Será preciso " + str(quantidadelatas) + " latas")
print("Custará " + str(valor) + " reais")
print(area)


