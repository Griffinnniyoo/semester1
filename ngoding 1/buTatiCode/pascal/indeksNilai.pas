program menghitungIndeksNilai;
{i.s : memasukan nilai }
{f.s : menampilkan hasil indeks nilai}

//kamus
uses crt;

var
       nilai : real;
       indeks : char;


begin

//badan program
textColor(yellow);
write('+++++++++++++++NILAI INDEKS+++++++++++++');
readln;
write('masukan nilai indeks :');
readln(nilai);
//jika bilangan input nya 79,9 maka hapus =(sama dengan) di < nya atau ganti variable type nya
//menjadi bilangan real
if (nilai >= 80) and (nilai <= 100 )
       then
       indeks := 'A'
       else 
          if (nilai >= 70) and (nilai <= 80 )
            then
              indeks := 'B'
            else  
              if (nilai >= 60) and (nilai <= 70 )
               then
                 indeks := 'C'
               else
                if (nilai >= 50) and (nilai <= 60 )
                  then
                    indeks := 'D'
                  else
                     indeks := 'E';
writeln('indeks :', indeks);
readln;
end.