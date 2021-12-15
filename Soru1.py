a=int(input("Üçgenin 1. kenarının x koordinatını giriniz"))
b=int(input("Üçgenin 2. kenarının y koordinatını giriniz"))

c=int(input("Üçgenin 2. kenarının x koordinatını giriniz"))
d=int(input("Üçgenin 2. kenarının y koordinatını giriniz"))

e=int(input("Üçgenin 3. kenarının x koordinatını giriniz"))
f=int(input("Üçgenin 3. kenarının y koordinatını giriniz"))

g=int(input("Kontrol etmek isteğiniz noktanın x koordinatını giriniz"))
h=int(input("Kontrol etmek isteğiniz noktanın y koordinatını giriniz"))

yatay=[a,c,e]
yatay.sort()
dikey=[b,d,f]
dikey.sort()

i=[*range(yatay[0],yatay[2])]
j=[*range(dikey[0],dikey[2])]

if (g in i) and (h in j):
    print("Üçgen içindedir")
else:
    print("Üçgen içinde değildir")