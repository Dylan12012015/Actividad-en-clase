numeros=[1,3,4,2,7,0]
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[i]+numeros[j]==10:
            print(numeros[i],"+",numeros[j])