program MenuPilihan;

uses crt, Math, SysUtils;

var
  pilih, angkaPertama, angkaKedua, N, i: Integer;
  opr: Char;
  hasil, a, b, c, hasil2, suku, S: Real;
  keterangan: String;

begin
  clrscr;
  writeln('PILIH MENU');
  writeln('-----------');
  writeln('1. Kalkulator sederhana');
  writeln('2. Suku ke N dari deret Fibonacci');
  writeln('3. S = 2/3 - 5/7 + 16/21 - 65/81 + ...');
  writeln('0. Keluar');
  write('Pilihan anda? : ');
  readln(pilih);

  while (pilih < 0) or (pilih > 3) do
  begin
    writeln('Nomor menu tidak ada, ulangi.');
    readln;
    clrscr;
    writeln('PILIH MENU');
    writeln('-----------');
    writeln('1. Kalkulator sederhana');
    writeln('2. Suku ke N dari deret Fibonacci');
    writeln('3. S = 2/3 - 5/7 + 16/21 - 65/81 + ...');
    writeln('0. Keluar');
    write('Pilihan anda? : ');
    readln(pilih);
  end;

  while pilih <> 0 do
  begin
    clrscr;
    case pilih of
      1: 
        begin
          writeln('<<<<<<<<<<<<< KALKULATOR SEDERHANA >>>>>>>>>>>>>');
          writeln;
          write('Masukkan angka pertama : ');
          readln(angkaPertama);
          write('Masukkan angka kedua : ');
          readln(angkaKedua);
          write('Masukkan operator (+, -, :, x) : ');
          readln(opr);

          while not (opr in ['+', '-', ':', 'x']) do
          begin
            writeln('Harus operator +, -, :, x. ULANGI!');
            readln;
            clrscr;
            writeln('<<<<<<<<<<<<< MASUKKAN ULANG OPERATOR >>>>>>>>>>>>>');
            writeln;
            write('Masukkan operator (+, -, :, x) : ');
            readln(opr);
          end;

          case opr of
            '+': hasil := angkaPertama + angkaKedua;
            '-': hasil := angkaPertama - angkaKedua;
            ':': hasil := angkaPertama / angkaKedua;
            'x': hasil := angkaPertama * angkaKedua;
          end;

          writeln;
          writeln('<<<<<<<<<<<<< HASIL KALKULATOR >>>>>>>>>>>>>');
          writeln('Angka pertama   = ', angkaPertama);
          writeln('Angka kedua     = ', angkaKedua);
          writeln('Operator        = ', opr);
          writeln('Hasil           = ', hasil:0:2);
        end;

      2: 
        begin
          writeln('<<<<<<<<<<<< SUKU KE-N DARI DERET FIBONACCI >>>>>>>>>>>>>');
          writeln;
          write('Masukkan nomor suku Fibonacci: ');
          readln(N);

          while N <= 0 do
          begin
            writeln('Masukkan nomor suku yang valid.');
            readln;
            clrscr;
            writeln('<<<<< MASUKKAN ULANG FIBONACCI >>>>>');
            writeln;
            write('Masukkan nomor suku Fibonacci: ');
            readln(N);
          end;

          a := 0;
          b := 1;
          if N = 1 then
            hasil2 := a
          else if N = 2 then
            hasil2 := b
          else
            for i := 2 to N do
            begin
              c := a + b;
              a := b;
              b := c;
            end;
          hasil2 := b;

          writeln('(Suku Ke-N dari Fibonacci)');
          writeln('Suku Ke : ', N);
          writeln('Suku Ke-', N, ' dari Deret Fibonacci adalah ', hasil2:0:2);
        end;

      3: 
        begin
          writeln('<<<<<<<<<<<< MENGHITUNG S DARI DERET >>>>>>>>>>>>>');
          writeln;
          write('Masukkan banyak suku (N): ');
          readln(N);

          while N <= 0 do
          begin
            writeln('Masukkan jumlah suku yang valid.');
            readln;
            clrscr;
            writeln('<<<<< MASUKKAN ULANG JUMLAH SUKU >>>>>');
            writeln;
            write('Masukkan banyak suku (N): ');
            readln(N);
          end;

          S := 0;
          keterangan := '';
          for i := 1 to N do
          begin
            suku := (5 * i * i * i - 26 * i * i + 46 * i - 23) / 
                    (6 * i * i * i - 31 * i * i + 55 * i - 27);

            if i mod 2 = 0 then
            begin
              S := S - suku;
              keterangan := keterangan + ' - (' + IntToStr(5 * i * i * i - 26 * i * i + 46 * i - 23) + '/' +
                       IntToStr(6 * i * i * i - 31 * i * i + 55 * i - 27) + ')';
            end
            else
            begin
              S := S + suku;
              if i = 1 then
                keterangan := '(' + IntToStr(5 * i * i * i - 26 * i * i + 46 * i - 23) + '/' +
                         IntToStr(6 * i * i * i - 31 * i * i + 55 * i - 27) + ')'
              else
                keterangan := keterangan + ' + (' + IntToStr(5 * i * i * i - 26 * i * i + 46 * i - 23) + '/' +
                         IntToStr(6 * i * i * i - 31 * i * i + 55 * i - 27) + ')';
            end;
          end;

          writeln('<<<< HASIL PERHITUNGAN >>>>');
          writeln('Banyak Suku (N) = ', N);
          writeln('S = ', keterangan);
          writeln('= ', S:0:3);
        end;
    end;

    readln;
    clrscr;
    writeln('PILIH MENU');
    writeln('-----------');
    writeln('1. Kalkulator sederhana');
    writeln('2. Suku ke N dari deret Fibonacci');
    writeln('3. S = 2/3 - 5/7 + 16/21 - 65/81 + ...');
    writeln('0. Keluar');
    write('Pilihan anda? : ');
    readln(pilih);
  end;
end.
