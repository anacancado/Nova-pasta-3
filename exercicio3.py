notas=[]
continua = True
while continua == True :
    nota= int(input("Insira a nota ou digie -1 para parar: "))
    if nota == -1:
        continua = False
    else:
        notas.append(nota)
media= sum(notas)/len(notas)
print("A media do aluno é igual a "+str(media))