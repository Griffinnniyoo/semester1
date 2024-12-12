program Barang;

uses crt;

var
  inputKodeBarang: string;
  jumlahBeliBarang: integer;
  diskonBarang: string;
  diberiDiskon: integer;
  diskon, hargaSatuanBarang, hargaTotal, totalBayar, bayar, kembalian: integer;
  namaBarang: string;

begin

  // Input
  Write('Masukan kode barang: ');
  ReadLn(inputKodeBarang);
  Write('Berapa jumlah yang anda beli: ');
  ReadLn(jumlahBeliBarang);

  // Tabel barang
  if (inputKodeBarang = 'PK01') then
  begin
    namaBarang := 'Pakaian';
    hargaSatuanBarang := 75000;
  end
  else if (inputKodeBarang = 'TS02') then
  begin
    namaBarang := 'Tas';
    hargaSatuanBarang := 65500;
  end
  else if (inputKodeBarang = 'SP03') then
  begin
    namaBarang := 'Sepatu';
    hargaSatuanBarang := 157000;
  end
  else if (inputKodeBarang = 'AK04') then
  begin
    namaBarang := 'Aksesoris';
    hargaSatuanBarang := 45000;
  end
  else
  begin
    WriteLn('Barang tidak ada dalam tabel!');
    Exit;
  end;

  // Menghitung harga total
  hargaTotal := hargaSatuanBarang * jumlahBeliBarang;

  // Input apakah ada diskon
  Write('Apakah ada diskon? [YA/TIDAK]: ');
  ReadLn(diskonBarang);

  diskon := 0;
  totalBayar := hargaTotal; // Inisialisasi totalBayar dengan hargaTotal
  bayar := hargaTotal; // Inisialisasi bayar dengan hargaTotal
  kembalian := totalBayar - bayar; // Inisialisasi kembalian dengan 0

  // Jika ada diskon
  if (diskonBarang = 'YA') then
  begin
    write('Masukan besaran diskon (%): ');
    ReadLn(diberiDiskon);

    // Diskon dihitung dari hargaTotal (bukan hargaSatuanBarang)
    diskon := hargaTotal * (diberiDiskon div 100); // Menghitung diskon berdasarkan harga total
    totalBayar := hargaTotal - diskon; // Mengurangi harga total dengan diskon

    // Bayar adalah jumlah yang dibayar, misalnya harga total jika belum dibayar.
    write('masukan uang cash anda :');
    readln(bayar);

    

    // Kembalian adalah sisa uang setelah pembayaran (totalBayar - bayar).
    kembalian := totalBayar - bayar; 
  end;

  // Output
  WriteLn('Kode Barang    : ', inputKodeBarang);
  WriteLn('Nama Barang    : ', namaBarang);
  WriteLn('Jumlah Beli    : ', jumlahBeliBarang);
  WriteLn('Harga Satuan   : Rp ', hargaSatuanBarang);
  WriteLn('Diskon         : Rp ', diskon, ' / ', diberiDiskon, '%');
  WriteLn('Harga Total    : Rp ', hargaTotal);
  WriteLn('Total Bayar    : Rp ', totalBayar);
  WriteLn('Bayar          : Rp ', bayar);
  WriteLn('Kembalian      : Rp ', kembalian);

  ReadLn;
end.
