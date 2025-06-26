from data import akun
from desainstruk import cetak_struk

def lihat_saldo():
    norek = input('Masukkan nomor rekening: ')
    pin = input('Masukkan PIN: ')
    
    if norek in akun and akun[norek]['pin'] == pin:
        print(f'Saldo Anda: Rp {akun[norek]['saldo']}')
    else:
        print('Nomor kartu atau PIN salah')

def tarik_tunai():
    norek = input('Masukkan nomor rekening: ')
    pin = input('Masukkan PIN: ')
    if norek in akun and akun[norek]["pin"] == pin:
        try:
            jumlah = int(input('Jumlah tarik tunai: '))
            if jumlah <= akun[norek]['saldo']:
                akun[norek]['saldo'] -= jumlah
                print(f'Berhasil tarik tunai Rp {jumlah}')
                cetak_struk(jumlah,norek,akun[norek]['saldo'],akun[norek]['nama'])
            else:
                print('Saldo tidak cukup')
        except ValueError:
            print('Input harus berupa angka')
    else:
        print('Nomor kartu atau PIN salah')

def ganti_pin():
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
