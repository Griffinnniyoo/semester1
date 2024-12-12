program hitungKaliMxN;
{i.s : pengguna memasukan nilai m dan n}
{f.s : menampilkan hasil penjumlahan antara m x n menggunakan op pertambahan}

uses crt;

var 
       M, N, i , Kali : integer; {i : adalah pencacah}

begin
       writeln('<<<<<<<<<<<<<PROGRAM_HITUNG_OP_++>>>>>>>>>>>>>');
       write('Masukan nilai M :'); readln(M);
       while (M < 0) or (M > 20) do
       begin
              write('Harga m harus dari 0 sampai 20 tekan enterrr!!!!');
              readln; clrscr;
       writeln('<<<<<<<<<<<<<PROGRAM_HITUNG_OP_++>>>>>>>>>>>>>');
       write('Masukan nilai M :'); readln(M);
       end;

       write('Masukan nilai N :'); readln(n);
       while (N < -5) or (M > 15) do
       begin
              write('Harga m harus dari -5 sampai 15 tekan enterrr!!!!');
              readln; clrscr;
       writeln('<<<<<<<<<<<<<PROGRAM_HITUNG_OP_++>>>>>>>>>>>>>');
       write('Masukan nilai M :', M);
       write('Masukan nilai N :'); readln(N);
       end;

end.