myArray=[1,2,1,3,3,1,2,1,5,1]
histograma={1:0,2:0,3:0,4:0,5:0}
for num in myArray:
    histograma[num] += 1
for num in sorted(histograma.keys()):
    print(str(num), ": ", "*" * histograma[num])