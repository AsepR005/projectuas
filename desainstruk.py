import datetime
waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def cetak_struk(jumlah, norek , saldo_akhir, nama):
    struk = f'''  
    =========== ASEPR BANK ===========
    -------- STRUK TRANSAKSI ---------
    Waktu       : {waktu}
    Transaksi   : Tarik Tunai
    Nomor Rek.  : {norek}
    Jumlah      : Rp {jumlah}
    Saldo akhir : Rp {saldo_akhir}
    Nama        : {nama}
    Terima kasih telah menggunakan ATM
    =================================='''

    buatfile =  open(r"D:\Tugas Semester 2\Dasar Pemograman\projectATM\struk.txt", 'a')
    buatfile.write(struk)
    buatfile.close()
