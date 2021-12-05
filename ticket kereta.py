import sys, os, time, random, getpass
def login() :
    batas = 3
    for a in range (batas) :
        print("==========================================")
        print("\tLogin User")
        print("==========================================")
        get_user = input("Username: ")
        get_password = getpass.getpass()

        sukses = False
        file = open('D:\Kampus\Logika & Algoritma\Project Algoritma\database_login.txt','r')
        for i in file :
            nama,usermame,password = i.split(',')
            password = password.strip()
            if(get_user == usermame) and (get_password == password) :
                sukses = True
                break
        if (sukses) :
            print("\nAnda Berhasil Login, Selamat Datang %s "%(nama))
            time.sleep(3)
            opsi = input("Apakah Anda Ingin Ke Menu Utama? (Y/N) : ")
            if opsi.lower() == 'y' :
                print("\nAnda Akan Di Alihkan Ke Menu Utama, Mohon Tunggu Sebentar")
                time.sleep(5)
                os.system("cls")
                list_menu()
            elif opsi.lower() == 'n' :
                print("\nAnda Keluar dari system Terima Kasih")
                time.sleep(5)
                os.system("cls")
                login()
            else :
                print("\nPilihan Tidak Tersedia")
            break
        else :
            print("\nMohon Maaf Username Dan Password Salah")
            a -=1
            time.sleep(5)
            os.system("cls")
    else :
        print("Mohon Maaf Anda Salah Memasukan Password Sebanyak %s Kali"%(batas))



def list_menu():
	print("=" * 36)
	print("Aplikasi Pesan Tiket Stasiun Bekasi")
	print("-" * 36)
	print("1. Pilih Kota Tujuan")
	print("2. Keluar Aplikasi")
	print("-" * 36)
	opsi=input("Masukkan Kata [1] Untuk Pembelian dan [2] Untuk Keluar dari System: ")
	if opsi.lower() == "1" :
		print("Silahkan Anda Memilih Destinasi Anda")
		time.sleep(2)
		os.system("cls")
	elif opsi.lower() == "2" :
		print("Anda Memilih Keluar Dari System, Terima Kasih")
		time.sleep(2)
		os.system("cls")
		exit()
	else :
		print("Mohon Maaf Pilihan Tidak Tersedia")
		time.sleep(3)
		os.system("cls")
		mulai()


def konfirmasi_pemesanan_ulang():
	pemesanan_ulang=input("Apakah anda ingin memesan tiket kembali? [Y/T] ... ")
	if pemesanan_ulang.lower() == "y" :
		print("Silahkan Anda Kembali Ke menu Utama")
		time.sleep(2)
		os.system("cls")
		list_menu()
	elif pemesanan_ulang() == "t" :
		print("Anda Memilih Keluar Dari System, Terima Kasih")
		time.sleep(2)
		os.system("cls")
		exit()
	else :
		print("Mohon Maaf Pilihan Tidak Tersedia")
		time.sleep(3)
		os.system("cls")
		mulai()


def pemesanan():
	print("-" * 36)
	print("Mengisi Data Pemesanan")
	print("-" * 36)
	print("Masukan Jumlah Tiket yang akan dipesan")
	beli_tiket = int(input("> Masukan Jumlah Tiket : "))
	list_nama_penumpang = list()
	print("Masukan Nama Penumpang Kereta Api")
	for urutanPemesan in range (beli_tiket):
		urutanPemesan += 1
		namaPemesan = input("> Masukan Nama Pemesan ke {} : ".format(urutanPemesan))
		list_nama_penumpang.append(str(namaPemesan)) 

	os.system("cls")

	
	total_harga_tiket = beli_tiket * harga_tiket
	
	print("-" * 46)
	print("   PT. Kereta API Indonesia - Stasiun Tegal   ")
	print("-" * 46)
	print("Kode Pemesanan Tiket : ", random.randint(1000,9999))
	print("Nama Kereta Api      : ", namaKereta)
	print("Kota Tujuan          : ", pilihan_kota)
	print("Nama Pemesan         : ".format(len(list_nama_penumpang)))
	for harga_tiket_dibeli in list_nama_penumpang:
		print (("- {}").format(harga_tiket_dibeli))
	print("-" * 46)
	print("Total Harga Tiket adalah","Rp.",(total_harga_tiket))
	print("-" * 46)
	print("")

def list_kota() :
	print("=" * 36)
	print("Daftar Tujuan Kota Tersedia")
	print("-" * 36)
	print("1. Semarang")
	print("2. Surabaya")
	print("3. Yogyakarta")
	print("-" * 36)

def pilih() :
    opsi=input("Masukkan Kata [Reg] [Login] [Exit] : ")
    if opsi.lower() == "reg" :
        print("Anda Memilih Registrasi User \nMohon Tunggu, Anda Akan Di Alihkan Ke Menu Register")
        time.sleep(2)
        os.system("cls")
        registerasi()
    elif opsi.lower() == "login" :
        print("Anda Memilih Login User \nMohon Tunggu, Anda Akan Di Alihkan Ke Menu Login")
        time.sleep(2)
        os.system("cls")
        login()
    elif opsi.lower() == "exit" :
        print("Anda Memilih Exit \nMohon Tunggu, Anda Akan Keluar dari Program")
        time.sleep(2)
        os.system("cls")
        print("Terima Kasih")
        time.sleep(2)
        exit()
    else :
        print("Mohon Maaf Pilihan Tidak Tersedia")
        time.sleep(3)
        os.system("cls")
        mulai()

def registerasi() :
    print("==========================================")
    print("\t Register User")
    print("==========================================")
    nama = input ("Masukan Nama Anda  : ")
    Username = input ("Masukan Username Anda : ")
    password = getpass.getpass()
    simpan(nama,Username,password)
    print("Data Berhasil Tersimpan")
    opsi = input("Apakah Anda Ingin Kembali Ke Menu Utama? (Y/N) : ")
    if opsi.lower() == 'y' :
        print("\nAnda Akan Di Alihkan Ke Menu Utama, Mohon Tunggu Sebentar")
        time.sleep(5)
        os.system("cls")
        login()
    elif opsi.lower() == 'n' :
        print("\nAnda Akan Kembali Ke Menu Utama")
        time.sleep(5)
        os.system("cls")
        start()


def simpan(nama,username,password) :
    file = open('D:\Kampus\Logika & Algoritma\Project Algoritma\database_login.txt','a')
    file.write("\n"+nama+","+username+","+password)
def start() :
    print("Selamat Datang Di System Pembelian TIKET \nSilahkan Masukkan KODE \n[Reg] Untuk Register \n[Login] Untuk Login User \n[Exit] Untuk Keluar System")
    pilih()

def mulai() :
	print("Selamat Datang Di System Pembelian Ticket PT.Kereta Api Indonesia")
	list_menu()
start()

list_kota()
pilihan_kota = input("Masukan Nama Kota Tujuan Anda : ")
print("-" * 36)
os.system("cls")
print("=" * 55)
print("Daftar Kereta Api yang Tersedia untuk Jurusan ", pilihan_kota)
print("-" * 55)
if(pilihan_kota == "Semarang" or pilihan_kota == "semarang"):
	print("1. Kaligung Eksekutif")
	print("2. Kamandaka")
	pilihan_kereta = int(input("Masukan Pilihan Kereta Anda : "))
	if(pilihan_kereta == 1):
		harga_tiket = 60000
		namaKereta = "Kaligung Eksekutif"
		os.system("cls")
		print("Kamu memilih Kereta Api KA Kaligung Eksekutif")
		pemesanan()
		konfirmasi_pemesanan_ulang()
	elif(pilihan_kereta == 2):
		harga_tiket = 50000
		namaKereta = "Kamandaka"
		os.system("cls")
		print("Kamu memilih Kereta Api KA Kamandaka")
		pemesanan()
		konfirmasi_pemesanan_ulang()
elif(pilihan_kota == "Surabaya" or pilihan_kota == "surabaya"):
		print("1. KA Jayabaya")
		print("2. KA Kertajaya")
		pilihan_kereta = int(input("Masukan Pilihan Kereta Anda : "))
		if(pilihan_kereta == 1):
			harga_tiket = 315000
			namaKereta = "KA Jayabaya"
			os.system("cls")
			print("Kamu memilih Kereta Api KA Jayabaya")
			pemesanan()
			konfirmasi_pemesanan_ulang()
		elif(pilihan_kereta == 2):
			harga_tiket = 150000
			namaKereta = "KA Kertajaya"
			os.system("cls")
			print("Kamu memilih Kereta Api KA Kertajaya")
			pemesanan()
			konfirmasi_pemesanan_ulang()
elif(pilihan_kota == "Yogyakarta" or pilihan_kota == "yogyakarta"):
		print("1. KA Fajar Utama")
		print("2. KA Senja Utama")
		pilihan_kereta = int(input("Masukan Pilihan Kereta Anda : "))
		if(pilihan_kereta == 1):
			harga_tiket = 300000
			namaKereta = "KA Fajar Utama"
			os.system("cls")
			print("Kamu memilih Kereta Api KA Fajar Utama")
			pemesanan()
			konfirmasi_pemesanan_ulang()
		elif(pilihan_kereta == 2):
			harga_tiket = 215000
			namaKereta = "KA Senja Utama"
			os.system("cls")
			print("Kamu memilih Kereta Api KA Senja Utama")
			pemesanan()
			konfirmasi_pemesanan_ulang()


        




