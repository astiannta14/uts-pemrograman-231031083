'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'Sistem Informasi C',
            '2023-2024',
            'S1',
            'aktif',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                             JURUSAN SAINS
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|
---------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |
---------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |
2   22A1210   | Matkul2                  |  3  | Selasa |
3   22A1211   | Matkul3                  |  3  | Rabu   |
4   22A1212   | Matkul4                  |  2  | Senin  |
5   22A1213   | Matkul5                  |  3  | Kamis  |
6   22A1214   | Matkul6                  |  3  | Kamis  |
7   22A1215   | Matkul7                  |  3  | Kamis  |
8   22A1216   | Matkul8                  |  2  | Kamis  |
---------------------------------------------------------
                        TOTAL SKS           21           
---------------------------------------------------------
|---------------------------57---------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!
BIO = ['Asti Ananta',
            '231031083',
            '14-Agustus-2005'
            'Sistem Informasi C',
            '2023-2024',
            'S1',
            'aktif',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']
print()
MK = [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan CINTA dan IMTAQ','Pengantar Pemograman','Pengantar Teknologi Informasi','Kalkulus Dasar 1','Sains Terpadu'],
        [2,2,2,2,3,3,3,3],
        ['Jumat','Jumat','Jumat','Kamis','Selasa','Jumat','Selasa','Rabu'],
        ['07.30-09.10','13.30-15.10','09.20-11.00','13.30-15.10','15.20-17.00','07.30-09.10','15.20-17.00']]
print()
# Data Mahasiswa
nama_lengkap = "Asti Ananta"
nim = "231031083"
TTL = "14-Agustus-2005"
program_prodi = "S1/Sistem Informasi C"
tahun_masuk = "2023 Ganjil"
status = "Aktif"

# Data Mata Kuliah
header_mk = ["No. Kode", "Mata Kuliah", "SKS", "Hari", "Jadwal"]
data_mk = [
    ["22A1209", "Agama Islam", 2, "Jumat", "07.30-09.10"],
    ["22A1210", "Pancasila", 2, "Jumat", "13.30-15.10"],
    ["22A1211", "Bahasa Indonesia", 2, "Jumat", "09.20-11.00"],
    ["22A1212", "Wawasan CINTA dan IMTAQ", 2, "Kamis", "09.20-11.00"],
    ["22A1213", "Pengantar Pemograman", 3, "Selasa", "13.30-15.10"],
    ["22A1214", "Pengantar Teknologi Informasi", 3, "Jumat", "15.20-17.00"],
    ["22A1215", "Kalkulus Dasar 1", 3, "Selasa", "07.30-09.10"],
    ["22A1216", "Sains Terpadu", 3, "Rabu", "15.20-17.00"]
]

# Menghitung statistik MK
total_sks = sum(row[2] for row in data_mk)
jumlah_mk = len(data_mk)
mk_2_sks = sum(1 for row in data_mk if row[2] == 2)
mk_3_sks = sum(1 for row in data_mk if row[2] == 3)
mk_senin = sum(1 for row in data_mk if row[3] == "Senin")
mk_selasa = sum(1 for row in data_mk if row[3] == "Selasa")
mk_rabu = sum(1 for row in data_mk if row[3] == "Rabu")
mk_kamis = sum(1 for row in data_mk if row[3] == "Kamis")

# Menampilkan Kartu Rencana Studi
print("           INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE")
print("                           JURUSAN SAINS")
print("                  KARTU RENCANA STUDI MAHASISWA")
print("                         GANJIL 2023/2024\n")
print(f"Nama Lengkap    : {nama_lengkap}")
print(f"NIM             : {nim}")
print(f"Program/prodi   : {program_prodi}")
print(f"Tahun Masuk     : {tahun_masuk}")
print(f"Status          : {status}\n")

# Tabel Mata Kuliah
print('-'*57)
print('No.'+'|'+'Kode'.ljust(10)+'|'+'mata kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|')
print('-'*57)
print('1. '+'|'+'22A1209'.ljust(10)+'|'+'kalkulus dasar'.center(26)+'|'+'3'.center(5)+'|'+'selasa'.center(8)+'|')
print('2. '+'|'+'22A1210'.ljust(10)+'|'+'pti'.center(26)+'|'+'2'.center(5)+'|'+'jumat'.center(8)+'|')
print('3. '+'|'+'22A1211'.ljust(10)+'|'+'bahasa'.center(26)+'|'+'3'.center(5)+'|'+'jumat'.center(8)+'|')
print('4. '+'|'+'22A1212'.ljust(10)+'|'+'cinta dan iptek'.center(26)+'|'+'2'.center(5)+'|'+'kamis'.center(8)+'|')
print('5. '+'|'+'22A1213'.ljust(10)+'|'+'sainster'.center(26)+'|'+'2'.center(5)+'|'+'rabu'.center(8)+'|')
print('6. '+'|'+'22A1214'.ljust(10)+'|'+'agama islam'.center(26)+'|'+'2'.center(5)+'|'+'jumat'.center(8)+'|')
print('7. '+'|'+'22A1215'.ljust(10)+'|'+'pemprograman'.center(26)+'|'+'3'.center(5)+'|'+'kamis'.center(8)+'|')
print('8. '+'|'+'22A1216'.ljust(10)+'|'+'pancasila'.center(26)+'|'+'3'.center(5)+'|'+'jumat'.center(8)+'|')
print('-'*57)

# Summary
print("Summary:")
print(f"Jumlah Mata Kuliah       : {jumlah_mk}")
print(f"Jumlah Mata Kuliah 2 SKS : {mk_2_sks} Mata Kuliah")
print(f"Jumlah Mata Kuliah 3 SKS : {mk_3_sks} Mata kuliah")
print(f"Mata Kuliah hari Senin   : {mk_senin} Mata Kuliah")
print(f"Mata Kuliah hari Selasa  : {mk_selasa} Mata Kuliah")
print(f"Mata Kuliah hari Rabu    : {mk_rabu} Mata Kuliah")
print(f"Mata Kuliah hari Kamis   : {mk_kamis} Mata Kuliah")
print(f"Mata Kuliah hari Jumat   : {0} Mata Kuliah\n")
print(" "*47 + "Parepare, 25 Oktober 2023")
print("\n" + " "*54 + f"{nama_lengkap}\n" + " "*54 + "-"*12)



