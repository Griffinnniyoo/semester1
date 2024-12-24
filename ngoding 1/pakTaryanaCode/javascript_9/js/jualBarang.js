const proses = () => {
       const kode_barang = document.form.kode_barang.value.toUppercase()
       const jumlah_beli_barang = document.form.jumlah_beli_barang.value
       const bayar_saldo = document.form.bayar_saldo.value

       if (kode_barang === 'PKO1') {
              nama_barang = 'pakaian'
              harga_barang = 70000
       } else if (kode_barang === 'TS02') {
              nama_barang = 'tas'
              harga_barang = 80000
       } else if (kode_barang === 'SP03') {
              nama_barang = 'sepatu'
              harga_barang = 90000
       } else if (kode_barang == 'AK04') {
              nama_barang = 'aksesoris'
              harga_barang = 100000
       } else {
              alert(`tidak ada barang seperti ${kode_barang}`)
       }

       
}