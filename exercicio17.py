num1 = int(input("Insira um valor: "))
num2 = int(input("Insira um valor: "))
num3 = int(input("Insira um valor: "))
if num1 > num2:
    if num1 > num3:
        print("O maior numero é o " + str(num1))
    else:
        print("O maior numero é o " + str(num3))
else: 
    if num2 > num3:
        print("O maior numero é o " + str(num2)) 
    else:
        print("O maior numero é o " + str(num3))