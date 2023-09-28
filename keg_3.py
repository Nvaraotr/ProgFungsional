# Hitung nilai akhir dengan bobot 40% UTS dan 60% UAS
def hitung_nilai_akhir(uts, uas):
    nilai_akhir = 0.4 * uts + 0.6 * uas
    return nilai_akhir

# Hitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua_mhs(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai['uts'], nilai['uas']
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Tampilkan nilai akhir mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa :")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}, Nilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Mahasiswa1': {'uts': 16, 'uas': 74},
        'Mahasiswa2': {'uts': 30, 'uas': 18},
        'Mahasiswa3': {'uts': 41, 'uas': 22},
    }

    data_nilai_akhir = hitung_nilai_akhir_semua_mhs(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()