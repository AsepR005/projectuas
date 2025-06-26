from data import akun

def tambah_akun():
    norek = input('Nomor kartu baru: ')
    if norek in akun:
        print('Akun sudah ada')
    else:
        pin = input('PIN:')
        nama = input('Nama:')
        saldo = int(input('Saldo awal: '))
        akun[norek] = {'pin': pin,'nama': nama,'saldo': saldo}
        print("Akun ditambahkan.")

def lihat_semua_akun():
    for norek, data in akun.items():
        print(f"{norek} - PIN: {data['pin']} - Nama: {data['nama']} - Saldo: Rp {data['saldo']}")

def edit_akun():
    norek = input('Masukkan nomor rekening : ')
    pin = input('Masukkan PIN : ')

    if norek in akun:
        if akun[norek]['pin'] == pin:
            pin_baru = input('Masukkan PIN baru: ')
            akun[norek]["pin"] = pin_baru
            print('PIN berhasil diubah')
        else:
            print('pin salah')
    else:
        print('Nomor rekening tidak ditemukan')

def tambah_saldo():
    norek = input('Masukkan nomor rekening : ')
    if norek in akun:
        try:
            tambah = int(input('Jumlah saldo yang ingin ditambahkan: '))
            akun[norek]["saldo"] += tambah
            print(f'Saldo berhasil ditambahkan. Saldo baru: Rp {akun[norek]['saldo']}')
        except ValueError:
            print('Jumlah harus berupa angka')
    else:
        print('Nomor rekening tidak ditemukan')

def hapus_akun():
    norek = input('Masukkan nomor rekening : ')
    pin = input('Masukkan nomor PIN: ')

    if norek in akun:
        if akun[norek]['pin'] == pin:
            konfirmasi = input(f'Yakin ingin menghapus akun {norek}? (y/n): ')
            if konfirmasi.lower() == 'y':
                del akun[norek]
                print('Akun berhasil dihapus')
            else:
                print('Penghapusan dibatalkan')
        else:
            print('PIN salah')
    else:
        print('Nomor rekening tidak ditemukan')    


    