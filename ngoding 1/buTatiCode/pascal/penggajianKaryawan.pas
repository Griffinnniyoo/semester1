program PenggajianKaryawan ;

{I.S. : pengguna nensaukan bulan dan tahun penggajiaan, tiga data karyawan yang terdiri dari NIK, nama, GajiPokok}
{F.S : menampilkan dara gaji perkaryawan dan total gaji yang harus dibayar}


//Kamus

var
       Bulan, Tahun, NIK1, NIK2, NIK3, Nama1, Nama2, Nama3 : string;
       GajiPokok1, GajiPokok2, GajiPokok3 : integer;
       PPN1, PPN2, PPN3, Tunjangan1, Tunjangan2, Tunjangan3 : real;
       GajiBersih1, GajiBersih2, GajiBersih3, TotalGaji :real;

//Badan Program
begin  
       //memasukan bulan dan tahun penggajian 
       write('Bulan (Nama Bulan :)'); readln(Bulan);
       write('Tahun (yyy :)'); readln(Tahun);

       //masukan penggajian karyawan kesatu
       writeln('<< Data KARYWAN Kesatu >>');
       write('Nomor Induk Karyawan (NIK) :'); readln(NIK1);
       write('Nomor Induk Karyawan (NAMA) :'); readln(Nama1);
       write('Nomor Induk Karyawan (GAJI POKOK) :'); readln(GajiPokok1);

       //menghitung gaji pajak tunjangan dan gaji bersih
       PPN1 := 0.1 * GajiPokok1;
       Tunjangan1 := 0.2 * GajiPokok1;
       GajiBersih1 := GajiPokok1 + Tunjangan1 - PPN1;
       writeln('Pajak PPN 10%    :RP ', PPN1:0:2);
       writeln('Tunjangan   20%    :RP ', Tunjangan1:0:2);
       writeln('Gaji Pokok  10%    :RP ', GajiPokok1:0:2); 
       writeln('Gaji bersih nya RP', GajiBersih1:0:2); 
       writeln('##########################################');
       

end.