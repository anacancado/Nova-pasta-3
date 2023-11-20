num=[]
continua = True
while continua == True :
    numero= int(input("Insira a nota ou digie -1 para parar: "))
    if numero == -1:
        continua = False
    else:
        num.append(numero)
numMenor=num[0]
for x in num:
    if x<numMenor:
        numMenor=x
print("O menor numero da lista é "+str(numMenor))