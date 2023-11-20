listaNum=[]
listaQuant=int(input("Sua lista terá quantos numeros? "))
i=0
while i<=(listaQuant-1):
    numero= int(input("Insura um numero a lista: "))
    listaNum.append(numero)
    i+=1
numMaior=0
for x in listaNum:
    if x>numMaior:
        numMaior=x
print("O maior numero da lista é "+str(numMaior))