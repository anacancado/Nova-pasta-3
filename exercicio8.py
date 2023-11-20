solicitUsuario = int(input("Digite um numero para calcularmos a sua tabuada: "))
i=0
while i<=10:
    result=i*solicitUsuario
    print(str(solicitUsuario) + "x" + str(i) + "=" + str(result))
    i+=1