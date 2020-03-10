import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:8008/") as proxy:
    print ("==Aplikasi Pemesanan Tiket Bisokop== \n")
    print ("1.Lihat daftar ")
    print ("2.Pesan tiket ")
    pil = int (input("Pilih nomer : "))

    if pil==1:
        print(proxy.lihat())

    elif pil== 2:
        inpt = input("Masukan nama film yang ingin dipesan : ")
        print(proxy.pesan(inpt))

