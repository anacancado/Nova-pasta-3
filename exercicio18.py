def ehprimo(i):
    j=1
    quantDiv=0
    while j<=i:
        if i%j==0:
            quantDiv+=1
        j+=1
    if quantDiv==2:
        return True
    return False
i=1
while i<=50:
    if ehprimo(i):
        print(i)
    i+=1