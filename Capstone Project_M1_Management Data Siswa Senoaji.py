#=====CAPSTONE MODULE 1========
#JCDS 3004 004 Senoaji Wicaksono

#data base utama
db_guru = {
    1: {"nama": "admin", 
        "nip" : 111,
        "username": "admin", 
        "password": "admin123"}
}

db_siswa = {
    1: {
        "nama": "chanatip songkarim",
        "nis": 1,
        "kelas": "10 IPA 1",
        "nilai": {
            "Biologi": 55,
            "Matematika": 90,
            "Kimia": 50
        },
        "username": "siswa1",
        "password": "siswa1"
    },
    2: {
        "nama": "kanda bahlil",
        "nis": 2,
        "kelas": "10 IPA 1",
        "nilai": {
            "Biologi": 80,
            "Matematika": 99,
            "Kimia": 90
        },
        "username": "siswa2",
        "password": "siswa2"
    },
    3: {
        "nama": "son goku",
        "nis": 3,
        "kelas": "10 IPA 1",
        "nilai": {
            "Biologi": 99,
            "Matematika": 99,
            "Kimia": 99
        },
        "username": "siswa3",
        "password": "siswa3"
}}
db_siswa_hapus = []


#fungsi -fungsi 

#menu login halaman awal
def menulogin():
    while True:
        print("\n=====Selamat Datang di Suzuran High School=====")
        print("1. Login Guru")
        print("2. Login Siswa")
        print("3. Exit")

        opsi = input("Masukan Opsi: ")
        if opsi == "1":
            guru_data = loginguru()
            if guru_data:
                menu_guru()
        elif opsi == "2":
            siswa_data = loginsiswa()
            if siswa_data:
                menu_siswa(siswa_data)
        elif opsi == "3":
            print("Terimakasih, Semoga Hari Anda Menyenangkan")
            break
        else:
            print("Kode yang anda masukan salah")

#login guru
def loginguru():
    print("\n=====Login Guru=====")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")

    for  nip,guru_data in db_guru.items():
        if guru_data['username'] == username and guru_data['password'] == password:
            print(f"\nLogin berhasil! Selamat datang {guru_data['nama']}")            
            return guru_data
    print("\nLogin gagal. Username atau password salah")


#menu guru
def menu_guru():
    while True:
        print("\n=== MENU GURU ===")
        print("1. Tampilkan Data Nilai")
        print("2. Tambah Data Siswa")
        print("3. Update Data Nilai")
        print("4. Hapus Data Siswa")
        print("5. Cek Kelulusan Siswa")  
        print("6. Logout")
        
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == "1":
            tampilkan_nilai_guru()
        elif pilihan == "2":
            tambah_siswa()
        elif pilihan == "3":
            update_nilai()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":  # Handle opsi baru
            tampilkan_kelulusan_siswa()
        elif pilihan == "6":
            print("Logout berhasil!")
            break
        else:
            print("Input salah!")

#tampilkan nilai untuk guru
def tampilkan_nilai_guru():
    print("\n=== Data Nilai Siswa ===")
    if not db_siswa:
        print("Tidak ada data siswa.")
        return
    
    for siswa_id, siswa_data in db_siswa.items():  # Mengunpack key dan value
        print(f"\nID: {siswa_id}")
        print(f"Nama: {siswa_data['nama']}")
        print(f"NIS: {siswa_data['nis']}")  # Diubah ke 'nis' untuk konsistensi
        print(f"Kelas: {siswa_data['kelas']}")
        for mata_pelajaran, nilai in siswa_data['nilai'].items():
            print(f"Nilai {mata_pelajaran}: {nilai}")

#tambah siswa
def tambah_siswa():
    print("\n=== TAMBAH DATA SISWA ===")
    while True:
        nama = input("Nama Siswa: ").strip()
        if nama.replace(" ", "").isalpha():  # Memperbolehkan spasi dalam nama
            break
        print("Nama harus berupa alpabet")
    while True:     # Validasi NIS (angka dan belum terdaftar)
        nis = input("NIS: ")
        if not nis.isdigit():   # harus integer
            print("NIS harus berupa angka")
            continue
        nis_terdaftar = False    # validasi nis
        for siswa_id, data in db_siswa.items():
            if str(data['nis']) == nis:
                nis_terdaftar = True
                break   
        if nis_terdaftar:
            print("NIS sudah terdaftar, input NIS lain")
        else:
            break
 
    kelas = input("Kelas: ")
    
    while True:     # Validasi username unik
        username = input("Username: ")
        username_terdaftar = any(data['username'] == username for data in db_siswa.values())

        if username_terdaftar:
            print("Username sudah digunakan, gunakan username lain")
        else:
            break
    password = input("Password: ")
    
    nilai = {}
    mata_pelajaran_list = ["Matematika", "Biologi", "Kimia"]  # Daftar mata pelajaran

    for mata_pelajaran in mata_pelajaran_list:
        while True:  # Loop sampai mendapatkan input yang valid
            input_nilai = input(f"Masukkan Nilai {mata_pelajaran} (0-100): ")
            
            if input_nilai.isdigit():  # Validasi 1: Cek apakah input adalah angka
                nilai_int = int(input_nilai)
                
                if 0 <= nilai_int <= 100:      # Validasi 2: Cek range nilai
                    nilai[mata_pelajaran] = nilai_int
                    break  # Keluar dari loop jika valid
                else:
                    print("Input nilai harus antara 0 dan 100")
            else:
                print("Input harus berupa angka")
    
    id_baru = max(db_siswa.keys()) + 1 if db_siswa else 1 #membuat id baru(as index) jika sudah ada +1 jika blm ada siswa di db maka 1
    db_siswa[id_baru] = {
        "nama": nama,
        "nis": nis,
        "kelas": kelas,
        "nilai": nilai,
        "username": username,
        "password": password
    }
    print(f"Data siswa berhasil ditambahkan dengan ID {id_baru}")

#update nilai siswa

def update_nilai():
    print("\n=== Update Data Nilai Siswa ===")
    
    print("\nDaftar Siswa:")     # Tampilkan dulu daftar siswa
    for siswa_id, siswa_data in db_siswa.items():
        print(f"ID: {siswa_id} | nis: {siswa_data['nis']} | Nama: {siswa_data['nama']}")
    
    while True:
        siswa_id_input = input("\nMasukkan ID siswa yang ingin diupdate: ")
        
        if not siswa_id_input.isdigit():
            print("Error: ID harus berupa angka!")
            continue
            
        siswa_id = int(siswa_id_input)
        
        if siswa_id not in db_siswa:
            print("Error: ID tidak ditemukan!")
            continue
            
        siswa_data = db_siswa[siswa_id]
        print(f"\nData Siswa: {siswa_data['nama']} (nis: {siswa_data['nis']}, Kelas: {siswa_data['kelas']})")
        
        for mata_pelajaran in siswa_data['nilai']:
            while True:
                input_nilai = input(f"Masukkan Nilai Baru {mata_pelajaran} (sebelumnya {siswa_data['nilai'][mata_pelajaran]}): ")
                
                if not input_nilai.isdigit():
                    print("Error: Input harus berupa angka bilangan bulat!")
                    continue
                    
                nilai_baru = int(input_nilai)
                
                if 0 <= nilai_baru <= 100:
                    siswa_data['nilai'][mata_pelajaran] = nilai_baru
                    break
                else:
                    print("Error: Nilai harus antara 0-100!")
        
        print("\nData nilai berhasil diupdate!")
        break

#fitur cek kelulusan

def cek_kelulusan(siswa_data):
    print(f"\n=== STATUS KELULUSAN {siswa_data['nama'].upper()} ===")
    print(f"NIS: {siswa_data['nis']}")
    print(f"Kelas: {siswa_data['kelas']}")
    
    total_nilai = 0
    jumlah_mapel = len(siswa_data['nilai'])
    
    print("\n{:<15} {:<10} {:<10}".format("Mata Pelajaran", "Nilai", "Status"))
    print("-"*35)
    
    for matpel, nilai in siswa_data['nilai'].items():
        status = "Lulus" if nilai >= 75 else "Tidak Lulus"
        total_nilai += nilai
        print("{:<15} {:<10} {:<10}".format(matpel, nilai, status))
    
    rata_rata = total_nilai / jumlah_mapel
    lulus = rata_rata >= 75
    
    print("\n{:<15} {:<10.2f}".format("Rata-rata", rata_rata))
    print("{:<15} {:<10}".format("Batas Kelulusan", ">= 75"))
    print("\nSTATUS AKHIR: ", "LULUS" if lulus else "TIDAK LULUS")
    return lulus

def tampilkan_kelulusan_siswa():
    print("\n=== CEK KELULUSAN SISWA ===")
    if not db_siswa:
        print("Tidak ada data siswa.")
        return
    
    print("\nDaftar Siswa:")
    for siswa_id, siswa_data in db_siswa.items():
        print(f"ID: {siswa_id} | NIS: {siswa_data['nis']} | Nama: {siswa_data['nama']}")
    
    while True:
        siswa_id_input = input("\nMasukkan ID siswa yang ingin dicek: ")
        
        if not siswa_id_input.isdigit():
            print("Error: ID harus berupa angka!")
            continue
            
        siswa_id = int(siswa_id_input)
        
        if siswa_id not in db_siswa:
            print("Error: ID tidak ditemukan!")
            continue
            
        siswa_data = db_siswa[siswa_id]
        cek_kelulusan(siswa_data)
        break


#hapus siswa
def hapus_siswa():
    print("\n=== HAPUS DATA SISWA ===")
    print("\nDaftar Siswa:")
    for siswa_id, siswa_data in db_siswa.items():
        print(f"ID: {siswa_id} | NIS: {siswa_data['nis']} | Nama: {siswa_data['nama']}")
    
    while True:
        siswa_id_input = input("\nMasukkan ID siswa yang ingin dihapus: ")
        
        if not siswa_id_input.isdigit():
            print(" ID harus berupa angka")
            continue
            
        siswa_id = int(siswa_id_input)
        
        if siswa_id not in db_siswa:
            print("ID tidak ditemukan!")
            continue
            
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus siswa ID {siswa_id}? (y/n): ").lower() #konfirmasi
        if konfirmasi != 'y':
            print("Penghapusan dibatalkan")
            return
            
        siswa_data = db_siswa[siswa_id]
        del db_siswa[siswa_id]  # Hapus permanen dari database
        
        print(f"\nData siswa {siswa_data['nama']} telah dihapus secara permanen!")
        break


#login siswa
def loginsiswa():
    print("\n=====Login Siswa=====")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")

    for siswa_id, siswa_data in db_siswa.items():  #cari key dan value
        if siswa_data['username'] == username and siswa_data['password'] == password:
            print(f"\nLogin berhasil! Selamat datang {siswa_data['nama']}")
            return siswa_data  # kembali ke data siswa 
    print("\nLogin gagal. Username atau password salah")

 #menu siswa       
def menu_siswa(siswa_data):
    while True:
        print("\n=== MENU SISWA ===")
        print(f"Selamat datang {siswa_data['nama']}")
        print("1. Lihat Nilai Saya")
        print("2. Cek Status Kelulusan")  # Opsi baru
        print("3. Logout")
        
        pilihan = input("Pilih menu (1-3): ")
        if pilihan == "1":
            tampilkan_nilai_siswa(siswa_data)
        elif pilihan == "2":
            cek_kelulusan(siswa_data)
        elif pilihan == "3":
            print("Logout berhasil!")
            break
        else:
            print("Input kurang!")

#tampilkan data nilai
def tampilkan_nilai_siswa(siswa_data):
    print("\n{:<15} {:<10}".format("Mata Pelajaran", "Nilai"))
    print("-"*25)
    for matpel, nilai in siswa_data['nilai'].items():
        print("{:<15} {:<10}".format(matpel, nilai))

menulogin()