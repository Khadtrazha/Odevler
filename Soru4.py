a=input("Metin giriniz")

b=[*a.split(" ")]

c=input("Metin içerisinde aramak istediğiniz kelimeyi yazınız")

if c in a:
    print("Kelime metin içerisinde bulunmaktadır")
else:
    print("Kelime metin içerisinde bulunmamaktadır")