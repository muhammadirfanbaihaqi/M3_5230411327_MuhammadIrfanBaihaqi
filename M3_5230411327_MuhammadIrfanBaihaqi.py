
listmakanan = []
listminuman = []

class Makanan:
    def __init__(self, makanan, harga) -> None:
        self.makanan = makanan
        self.harga = harga

    def tampilmenumakan(self):
        print(f"{self.makanan} ==> {self.harga}")


class Minuman:
    def __init__(self,minuman, harga) -> None:
        self.minuman = minuman
        self.harga = harga

    def tampilminuman(self):
        print(f"{self.minuman} ==> {self.harga}")


def tampilmenuutama():
    print("\n=====SELAMAT DATANG=====")
    print("1. TAMPIL DAFTAR MAKANAN")
    print("2. TAMPIL DAFTAR MINUMAN")
    print("3. TAMBAH MENU")
    print("0. Keluar")
    print("=========================")

def Dsiplaysubmenutambah():
    print("\n=====================")
    print("1. TAMBAH MAKANAN")
    print("2. TAMBAH MINUMAN")
    print("0. Keluar")
    print("======================")

def submenutambah():
    while True:
        Dsiplaysubmenutambah()
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "1":
            while True:
                objek = input("Masukkan nama object: ")
                makanan = input("Masukkan nama makanan: ")
                hargastr = input("Masukkan harga makanan: ")
                cekint = hargastr.isdigit()
                if (type(makanan) == str and cekint == True):
                    harga = int(hargastr)
                    objek = Makanan(makanan,harga)
                    listmakanan.append(objek)
                    print("MENU SUDAH DITAMBAHKAN\n")
                    break
                else:
                    print("INPUTAN ANDA SALAH")
                    continue
        elif pilihan == "2":
            while True:
                objek = input("Masukkan nama object: ")
                minuman = input("Masukkan nama minuman: ")
                hargastr = input("Masukkan harga minuman: ")
                cekint = hargastr.isdigit()
                if (type(minuman) == str and cekint == True):
                    harga = int(hargastr)
                    objek = Minuman(minuman,harga)
                    listminuman.append(objek)
                    print("MENU SUDAH DITAMBAHKAN\n")
                    break
                else:
                    print("INPUTAN ANDA SALAH")
                    continue
        elif pilihan == "0":
            return True
        else:
            print("PILIHAN ANDA SALAH")
            continue


def menu():
    while True:
        tampilmenuutama()
        pilihmenu = input("Masukkan Pilihan menu: ")
        if pilihmenu == "1":
            if listmakanan == []:
                print("MENU MASIH KOSONG")
            print(f"=========DAFTAR MAKANAN=======")
            for i in listmakanan:
                i.tampilmenumakan()
            print("===========================\n")
        elif pilihmenu == "2":
            if listminuman == []:
                print("MENU MASIH KOSONG")
            print(f"========DAFTAR MINUMAN========")
            for i in listminuman:
                i.tampilminuman()
            print("===========================\n")
        elif pilihmenu == "3":
            submenutambah()
        elif pilihmenu == "0":
            print("ANDA KELUAR PROGRAM")
            break
        else:
            print("PILIHAN ANDA SALAH")
            continue

# DEFAULT MAKANAN
bakmi = Makanan("Bakmi", 20000)
soto = Makanan("Soto", 10000)
nasi_goreng = Makanan("Nasi Goreng", 20000)
listmakanan.append(bakmi)
listmakanan.append(soto)
listmakanan.append(nasi_goreng)

# DEFAULT MINUMAN
teh_panas = Minuman("TEH PANAS", 5000)
jeruk_panas = Minuman("JERUK PANAS", 5000)
Kopi = Minuman("Kopi", 5000)
listminuman.append(teh_panas)
listminuman.append(jeruk_panas)
listminuman.append(Kopi)
menu()





        