n=int(input("Digite o qtd: "))
n1=0
n2=1
print(n1)
print(n2)
for x in range(1,n-1):
    resposta=n1+n2
    n1 = n2
    n2=resposta
    print(resposta)