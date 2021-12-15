a=int(input("Sayý giriniz"))

b=[*range(1,a+1)]

bolenler=[]

for i in b :
    
    if a%i==0:
        bolenler.append(i)
    
print(bolenler)