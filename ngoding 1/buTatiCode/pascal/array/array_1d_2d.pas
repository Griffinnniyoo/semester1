program Array1D2D; 
uses crt;

// Konstanta
const
  MaksAngka = 10;
  MaksBaris = 5;
  MaksKolom = 3;

// Tipe Data
type
  ArrayAngka = array[1..MaksAngka] of integer;
  Matriks = array[1..MaksBaris, 1..MaksKolom] of integer;

// Variabel Global
var
  Angka: ArrayAngka;
  A: Matriks;
  Pilih, Pilih1, Pilih2: integer;

// Prosedur Menu Utama
procedure MenuUtama(var Pilih: integer);
begin
  writeln('<<<<<<<< MENU >>>>>>>>');
  writeln('1. ARRAY SATU DIMENSI');
  writeln('2. ARRAY DUA DIMENSI');
  writeln('0. KELUAR');
  write('Pilihan Anda: ');
  readln(Pilih);
end;

// Prosedur Menu Array 1D
procedure MenuArray1D(var Pilih1: integer);
begin
  writeln('<<<<<<<< MENU Array 1D >>>>>>>>');
  writeln('1. PENGISIAN ARRAY 1 DIMENSI');
  writeln('2. PENAMBAHAN ELEMEN ARRAY');
  writeln('3. PENYISIPAN ELEMEN ARRAY');
  writeln('4. PENGHAPUSAN ELEMEN ARRAY');
  writeln('5. PENYAJIAN ELEMEN ARRAY');
  writeln('0. KELUAR');
  write('Pilihan Anda: ');
  readln(Pilih1);
end;

// Prosedur Menu Array 2D
procedure MenuArray2D(var Pilih2: integer);
begin
  writeln('<<<<<<<< MENU Array 2D >>>>>>>>');
  writeln('1. PENGISIAN MATRIKS');
  writeln('2. PENYAJIAN MATRIKS');
  writeln('0. KELUAR');
  write('Pilihan Anda: ');
  readln(Pilih2);
end;

// Prosedur Penciptaan Array 1D
procedure PenciptaanAngka(var Angka: ArrayAngka);
var
  i: integer;
begin
  for i := 1 to MaksAngka do
    Angka[i] := 0;
end;

// Prosedur Tampil Angka
procedure TampilAngka(Angka: ArrayAngka; BanyakData: integer);
var
  i: integer;
begin
  for i := 1 to BanyakData do
    writeln('Angka [', i, '] = ', Angka[i]);
end;

// Prosedur Penciptaan Matriks
procedure PenciptaanMatriks(var A: Matriks);
var
  i, j: integer;
begin
  for i := 1 to MaksBaris do
    for j := 1 to MaksKolom do
      A[i, j] := 0;
end;

// Prosedur Tampil Matriks
procedure TampilMatriks(A: Matriks);
var
  i, j: integer;
begin
  for i := 1 to MaksBaris do
  begin
    for j := 1 to MaksKolom do
      write(A[i, j]:5);
    writeln;
  end;
end;

// Program Utama
begin
  clrscr;
  Pilih := -1;
  while Pilih <> 0 do
  begin
    MenuUtama(Pilih);
    clrscr;
    case Pilih of
      1:
        begin
          MenuArray1D(Pilih1);
          PenciptaanAngka(Angka);
          while Pilih1 <> 0 do
          begin
            clrscr;
            case Pilih1 of
              1: writeln('Pengisian Array Belum Terimplementasi');
              5: TampilAngka(Angka, MaksAngka);
            end;
            writeln('Tekan Enter untuk kembali ke menu');
            readln;
            MenuArray1D(Pilih1);
          end;
        end;
      2:
        begin
          MenuArray2D(Pilih2);
          PenciptaanMatriks(A);
          while Pilih2 <> 0 do
          begin
            clrscr;
            case Pilih2 of
              1: writeln('Pengisian Matriks Belum Terimplementasi');
              2: TampilMatriks(A);
            end;
            writeln('Tekan Enter untuk kembali ke menu');
            readln;
            MenuArray2D(Pilih2);
          end;
        end;
    end;
    clrscr;
  end;
  writeln('Program Selesai.');
end.
