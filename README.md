
# Project Title

A brief description of what this project does and who it's for

#  Sistem Manajemen Siswa - Suzuran High School

Sistem manajemen siswa berbasis **Python** untuk **Suzuran High School** yang memungkinkan guru dan siswa mengakses informasi akademik.

---

## Gambaran Umum

Guru dapat mengelola data siswa, nilai, dan memeriksa status kelulusan, sementara siswa dapat melihat nilai mereka sendiri dan status kelulusan.

---

##  Fitur

###  Fitur Guru

-  **Sistem Login**: Login aman dengan username dan password
-  **Lihat Nilai Siswa**: Menampilkan semua nilai siswa dalam sistem
-  **Tambah Siswa Baru**: Menambahkan data siswa baru beserta nilainya
- **Perbarui Nilai**: Memodifikasi nilai siswa yang ada
-  **Hapus Siswa**: Menghapus data siswa (penghapusan permanen)
-  **Cek Status Kelulusan**: Melihat apakah siswa memenuhi kriteria kelulusan

###  Fitur Siswa

-  **Sistem Login**: Login aman dengan username dan password
-  **Lihat Nilai Pribadi**: Hanya melihat nilai mereka sendiri
-  **Cek Status Kelulusan**: Memverifikasi apakah mereka memenuhi syarat kelulusan

---

## Struktur Data

###  Database Guru 
Menyimpan kredensial guru:
- NIP (ID Guru)
- Nama
- Username
- Password

### Database Siswa 

Menyimpan informasi lengkap siswa:
- ID Siswa
- NIS (Nomor Induk Siswa)
- Nama
- Kelas
- Nilai (Biologi, Matematika, Kimia)
- Kredensial login (Username dan Password)

---

## Cara Menggunakan

1. **Jalankan Program**: Eksekusi script Python 
2. **Menu Utama**:
   - Login sebagai Guru
   - Login sebagai Siswa
   - Keluar

### Akses Guru

- Kredensial admin default:
  - Username: `admin`
  - Password: `admin123`
- Setelah login, guru dapat mengakses semua fitur manajemen siswa.

### Akses Siswa

- Contoh kredensial siswa tersedia dalam database
- Siswa hanya dapat melihat informasi mereka sendiri

---

## Catatan

- Semua data **disimpan di memori** (tidak bertahan antar sesi)
- Nilai kelulusan minimum adalah **75** untuk semua mata pelajaran
- Siswa harus **lulus semua mata pelajaran** untuk bisa lulus

---

## Data Contoh

Sistem ini telah dilengkapi dengan data awal:

- 1 akun guru (admin)
- 3 akun siswa dengan nilai contoh

---

---

## CRUD (Create, Read, Update, Delete)

Proyek ini mengikuti prinsip **CRUD** (Create, Read, Update, Delete) sebagai berikut:

- **Create**  
  Admin dapat **menambahkan siswa baru** ke dalam database.

- **Read**  
  Admin dan siswa dapat **melihat data siswa** yang ada sesuai hak akses masing-masing.

- **Update**  
  Admin dapat **mengubah informasi siswa**, termasuk memberikan **remidi** untuk siswa yang tidak lulus.

- **Delete**  
  Admin dapat **menghapus data siswa** dari database.  
  Data yang dihapus akan **disimpan dalam backup** untuk keperluan referensi di masa mendatang.

> Dengan sistem ini, diharapkan manajemen data siswa menjadi lebih **efisien**, **aman**, dan **terorganisir**.


