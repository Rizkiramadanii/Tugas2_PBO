# membuat class mahasiswa yang berisi nama,nim dan jurusan
class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama Mahasiswa:", self.nama)
        print("NPM:", self.npm)
        print("Jurusan:", self.jurusan.NamaJurusan)

# membuat kelas jurusan yang mana berfungsi untuk menampilkan daftar mahasiswa yang ada pada suatu jurusan
# yang menampilkan nama dan nim nya
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("\nDaftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("- Nama:", mahasiswa.nama)
            print("  NPM:", mahasiswa.npm)

# membuat kelas universitas yang mana class ini berfungsi agar kita bisa menambahkan jurusan dan menampilkannya 
# pada daftar jurusan yang ada
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("- Jurusan:", jurusan.NamaJurusan)

# membuat objek universitas xyz yang mana merupakan universitas bengkulu
universitas_xyz = Universitas("Bengkulu")

# menambahkan objek berupa jurusan pada program
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)
jurusan_akun = Jurusan("Akuntansi")
universitas_xyz.tambah_jurusan(jurusan_akun)
jurusan_stat = Jurusan("Statistika")
universitas_xyz.tambah_jurusan(jurusan_stat)

# menambahkan data mahasiswa yang ingin kita masukkan baik nama,npm serta jurusannya
# jurusan TI
mahasiswa1 = Mahasiswa("Rizki Ramadani Dalimunthe", "G1A022054", jurusan_ti)
mahasiswa2 = Mahasiswa("Reksi Hendra Pratama", "G1A022032", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa1)
jurusan_ti.tambah_mahasiswa(mahasiswa2)

# menambahkan data mahasiswa jurusan akuntansi
mahasiswa3 = Mahasiswa("Gading Wonopati","C1C022067",jurusan_akun)
jurusan_akun.tambah_mahasiswa(mahasiswa3)

# menambahkan data mahasiswa jurusan statistika
mahasiswa4 = Mahasiswa("Ranisyah anggraini","F1F022018",jurusan_stat)
jurusan_stat.tambah_mahasiswa(mahasiswa4)

# memanggil fungsi sekaligus menampilkan jurusan yang ada di universitas bengkulu
universitas_xyz.tampilkan_daftar_jurusan()

# memanggil fungsi serta menampilkan daftar mahasiswa yang ada pada jurusan masing masing
jurusan_ti.tampilkan_daftar_mahasiswa()
jurusan_akun.tampilkan_daftar_mahasiswa()
jurusan_stat.tampilkan_daftar_mahasiswa()