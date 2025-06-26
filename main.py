from tampilan_menu import menu_nasabah,menu_admin
from eksmenu_nasabah import lihat_saldo,tarik_tunai,ganti_pin
from eksmenu_admin import tambah_akun,lihat_semua_akun,edit_akun,tambah_saldo,hapus_akun


def mulai():
    while True:
        menu_nasabah()
        menu = input('Pilihlah Dari 1-4 : ')

        if menu == '1':
            lihat_saldo()

        elif menu == '2':
            tarik_tunai()

        elif menu == '3':
            ganti_pin()
        
        elif menu == '4':
            print('Terima kasih')
            break
        
        elif menu == 'admin':
            password = input('Masukan Password: ')
            if password == '123':
                print('Login berhasil')
                while True :
                    menu_admin()
                    pilihan = input('Pilih 1-6: ')

                    if pilihan == '1':
                        tambah_akun()
                    elif pilihan == '2':
                        lihat_semua_akun()
                    elif pilihan == '3':
                        edit_akun()
                    elif pilihan == '4':
                        tambah_saldo()
                    elif pilihan == '5':
                        hapus_akun()
                    elif pilihan == '6':
                        print('kembali')
                        break
                    else:
                        print('pilihan salah')

            else:
                print('Password salah')

        else:
            print('Pilihan anda salah')

if __name__ == '__main__':
    mulai()     