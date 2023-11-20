numero=int(input("Insira um numero para calcularmos o fatorial: "))
i=1
j=1
while i<=numero:
    j=j*i
    i+=1
print("O fatorial de "+ str(numero) + " é "+str(j)+".")