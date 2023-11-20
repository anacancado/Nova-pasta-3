x=int(input("Insira o valor de x: "))
y=int(input("Insira o valor de y: "))
if x>0 and y>0:
    print("O ponto esta no primeiro quadrante.")
elif x<0 and y>0:
    print("O ponto esta no segundo quadrante.")
elif x<0 and y<0:
    print("O ponto esta no terceiro quadrante.")
else:
    print("O ponto esta no quarto quadrante.")