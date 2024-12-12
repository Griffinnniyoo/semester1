program hitungPemiluANJAAAYYY;
{i:s : memasukan input umurrr}
{f:s : hasilkan memilih atau tidak}

//kamus
var
       umur : integer;
       menikah : string;


begin
write('masukan umur anda kocagg :');      
readln(umur);
if (umur <= 17)
       then
       write('apakah anda sudah menikah :');
       readln(menikah);
       menikah := upcase(menikah);
              if (menikah = 'Y')
                     then
                            writeln('anda boleh ikut pemilu')
                     else
                            writeln('anda ga boleh ikut pemilu');
                            
                     else
                     write('anda boleh ikut pemilu')
readln;
end.



