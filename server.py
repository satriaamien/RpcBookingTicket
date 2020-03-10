from xmlrpc.server import SimpleXMLRPCServer

film=[["naruto",50000,5],["sasuke",40000,5],["one piece",45000,5],["Dota 2",50000,5],["Batman",40000,5]]

with SimpleXMLRPCServer(("127.0.0.1", 8008))as server:
    server.register_introspection_functions()#ini buat daftarin list method

    print('mulai menghubungkan port 8008...')

    def lihat():
        return film
    server.register_function(lihat, "lihat")
    
    def cari_ubah_judul(x,judul):
        hasil = ("tidak ada")
        for i in film:
            if x==i[0]:
                i[0]= judul
                hasil = ("Data berhasil di ubah")           
        return hasil
    server.register_function(cari_ubah_judul, "cari_ubah_judul")

    def cari_ubah_harga(x,harga):
        hasilnya = ("tidak ada")
        for i in film:
            if x==i[0]:
                i[1]= harga
                hasilnya = ("Data berhasil di ubah")           
        return hasilnya
    server.register_function(cari_ubah_harga, "cari_ubah_harga")

    def pesan(x):
        hasilnya = ("tiket telah habis")
        for i in film:
            if x==i[0]:
                if i[2]>0:
                    i[2] = i[2]-1 
                    hasilnya = ("Tiket telah dipesan")
        return hasilnya
    server.register_function(pesan, "pesan")

    server.serve_forever()