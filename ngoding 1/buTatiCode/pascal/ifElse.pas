program menantukanGenapGanjil;
{i.s : pengguna menampilkan sebuah bilangan}
{f.s : menampilkan keterangan bilangan genap atau bilangan ganjil}
var 
       bilangan  : integer;
       keterangan : string;
begin
       writeln('\\\\\\\\ PEMROGRAMAN MENENTUKAN GENAP DAN GANJIL \\\\\\\\\\');
       write('masukan bilangan :');readln(bilangan);
       //menentukan bikangan genap atau ganjil
   
       if (bilangan mod 2 = 0)
              then 
                     keterangan:= 'bilangan genap'
                     //kalo ada else gabole ada titik koma(;) sebelumnya
              else 
                     keterangan := 'bilangan ganjil';
       writeln('hasilnya adalah : ', bilangan, ' adalah ', keterangan)

end.