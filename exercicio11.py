ladoA=int(input("Insira o valor do primeiro lado do triangulo: "))
ladoB=int(input("Insira o valor do segundo lado do triangulo: "))
ladoC=int(input("Insira o valor do terceiro lado do triangulo: "))
if ladoA==ladoB and ladoA==ladoC and ladoB==ladoC:
    print("Esse triangulo é equilatero.")
elif ladoA!=ladoB and ladoA!=ladoC and ladoB!=ladoC:
    print("Esse triangulo é escaleno.")
else:
    print("Esse triangulo é isosceles.")