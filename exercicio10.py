listaNum=[]
listaQuant=int(input("Sua lista terá quantos numeros? "))
i=0
while i<=(listaQuant-1):
    numero= int(input("Insura um numero a lista: "))
    listaNum.append(numero)
    i+=1
numPar=0
numIm=0
for x in listaNum:
    if x%2==0:
        numPar+=1
    else:
        numIm+=1
print ("Na lista existem "+ str(numPar)+" numeros pares e "+str(numIm)+" numeros impares.")