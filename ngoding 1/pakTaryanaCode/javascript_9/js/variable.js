const proses = () =>{
       const namaBarang = document.form.namaBarang.value.toUpperCase()
       const hargaSatuan = document.form.hargaSatuan.value
       const jumlahBeli = document.form.jumlahBeli.value
       const hargaAwal = jumlahBeli * hargaSatuan
       document.form.hargaAwal.value = hargaAwal
       if (namaBarang == 'LE MINERAL') {
           besarDiskon = 0.1
       } else if (namaBarang == 'AQUA') {
           besarDiskon = 0.2
       } else {
           besarDiskon = 0
       }
       
       if (hargaAwal > 100000) {
           besarDiskon += 0.1
       }
       
       document.form.besarDiskon.value = parseInt(besarDiskon * 100) + '%'
   
       const totalDiskon = hargaAwal * besarDiskon
       document.form.totalDiskon.value = parseInt(totalDiskon)
   
       const totalHarga = hargaAwal - totalDiskon
       document.form.totalHarga.value = totalHarga
   
       const jumlahBayar = document.form.jumlahBayar.value
       const jumlahKembalian = jumlahBayar - totalHarga
       if (jumlahBayar == 0) {
           jumlahKembalian = 0
       }
       document.form.jumlahKembalian.value = jumlahKembalian
   }