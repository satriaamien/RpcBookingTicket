import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8008/") as proxy:
    print ("==Aplikasi Pemesanan Tiket Bisokop== \n")
    print ("1.ubah nama judul ")
    print ("2.lihat daftar ")
    print ("3.ubah harga ")
    pil = int (input("Pilih nomer : "))
    
    if pil==1:
        inpt = input("Masukan nama film yang di cari : ")
        inpt2 = input("masukan judul baru : ")
        print(proxy.cari_ubah_judul(inpt,inpt2))
    elif pil==2:
        print(proxy.lihat())
    elif pil==3:
        inpt = input("Masukan nama film yang di cari : ")
        inpt2 = input("masukan harga baru : ")
        print(proxy.cari_ubah_harga(inpt,inpt2))
