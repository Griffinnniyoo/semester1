program menghitungIndeksNilai;
{i.s : memasukan nilai }
{f.s : menampilkan hasil indeks nilai}

//kamus
uses crt;

var
       nilai : integer;
       indeks : string;


begin

//badan program
textColor(yellow);
write('+++++++++++++++NILAI INDEKS+++++++++++++');
readln;
write('masukan nilai indeks :');
readln(nilai);
//jika bilangan input nya 79,9 maka hapus =(sama dengan) di < nya atau ganti variable type nya
//menjadi bilangan real
//menyederhanakan bentuk if
case (nilai) of
       80..100 : indeks := 'A';
       70..79 : indeks := 'B';
       60..69 : indeks := 'C';
       50..59 : indeks := 'D';
       0..49 : indeks := 'E';
       else
       indeks := 'nilai hanya antara 0-100 BUANGSATTTTT!!!';
end; //end

writeln('indeks :', indeks);
readln;
end.