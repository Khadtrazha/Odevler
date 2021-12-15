import socket

Port = 123  
Soket = socket.socket() 
Host = '127.0.0.1';
Soket.bind((Host, Port))  
Soket.listen(5)  

print("Alıcı Bekleniyor...")

while True:
	conn, addr = Soket.accept()  
	print(f"Bağlanıldı {addr}")
	Veri = conn.recv(1024)
	conn.send(b"image.jpeg"); 
	print(f"Karşılama Mesajı Alındı {Veri}")
	with open("image.jpeg", "rb") as dosya:
		Veri = dosya.read(1024)
		while Veri:
			conn.send(Veri)
			print(f"Aktarılıyor {Veri!r}")
			Veri = dosya.read(1024)

	print("Aktarım Tamamlandı.")
	conn.close() 

Soket.shutdown(1)
Soket.close()