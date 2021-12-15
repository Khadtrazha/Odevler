import socket
 
Soket = socket.socket()  
Host = '127.0.0.1';
Port = 123 
 
Soket.connect((Host, Port))
Soket.send(b"Merhaba!")
Veri = Soket.recv(1024);
DosyaAdi = "İndirilen-"+str(Veri.decode("utf-8")); 
with open(b"image.jpeg", "wb") as dosya:
	print("Dosya Transfer Ediliyor.")
	while True:
		Veri = Soket.recv(1024)
		if not Veri:
			break
		dosya.write(Veri)  
 
print("Dosya Başarıyla Alındı.")
Soket.close()