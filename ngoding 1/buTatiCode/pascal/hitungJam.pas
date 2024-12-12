var
       jamKerja, totalUpah: integer;

const 
       upahPerjam = 10000;
begin
       write('Masukkan jam kerja Anda: '); 
       readln(jamKerja);


       totalUpah := jamKerja * upahPerjam;

       if jamKerja > 40 then
              totalUpah := totalUpah + (jamKerja - 40) * upahPerjam;

       writeln('Total upah Anda adalah: ', totalUpah);
end.
