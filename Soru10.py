from matplotlib import pyplot as plt
a=[]
b=[]
f=[]
i=0

while i != 10:
    i+=1
    c=input("Öğrencinin ismini giriniz")
    a.append(c)
    d=int(input("Öğrencinin boyunu giriniz (cm)"))
    b.append(d)
    d=int(input("Öğrencinin kilosunu giriniz (kg)"))
    f.append(d)

plt.bar(a,b)
plt.legend()
plt.xlabel(" ")
plt.ylabel("Boy (cm)")
plt.title("Boy")
plt.show()

plt.bar(a,f)
plt.legend()
plt.xlabel(" ")
plt.ylabel("Kilo (kg)")
plt.title("Kilo")
plt.show()