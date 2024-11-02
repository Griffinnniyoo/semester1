program hitungBiayaParkir;
uses crt;

// Kamus
var 
    kendaraan, nomorPolisi: string;
    jamMasuk, menitMasuk, jamKeluar, menitKeluar: integer;
    jam, menit, biaya: integer;

// Badan program
begin
    write('Masukkan jenis kendaraan (motor/mobil): ');
    readln(kendaraan);
    write('Masukkan nomor polisi: ');
    readln(nomorPolisi);
    
    write('Masukkan jam masuk : ');
    readln(jamMasuk);
    write('Masukkan menit masuk : ');
    readln(menitMasuk);
    
    write('Masukkan jam keluar : ');
    readln(jamKeluar);
    write('Masukkan menit keluar : ');
    readln(menitKeluar);
    
    // Menentukan lama parkir
    if (menitKeluar < menitMasuk) then
    begin
        menitKeluar := menitKeluar + 60;
        jamKeluar := jamKeluar - 1; 
    end;

    menit := menitKeluar - menitMasuk;  
    if (jamKeluar < jamMasuk) then
    begin
        jamKeluar := jamKeluar + 12;
    end;

    jam := jamKeluar - jamMasuk;

    if (menit > 0) then
        jam := jam + 1;

    // Menghitung biaya parkir
    if (kendaraan = 'motor') then 
        biaya := 1500 + (jam - 1) * 500
    else
        biaya := 3500 + (jam - 1) * 500;

    // Menampilkan hasil
    writeln('Jenis kendaraan: ', kendaraan);
    writeln('Nomor polisi: ', nomorPolisi);
    writeln('Jam masuk: ', jamMasuk,':', menitMasuk);
    writeln('Jam keluar: ', jamKeluar,':',  menitKeluar);
    writeln('Lama parkir: ', jam, ' jam ', menit, ' menit');
    writeln('Biaya parkir: Rp ', biaya);
  
end.
