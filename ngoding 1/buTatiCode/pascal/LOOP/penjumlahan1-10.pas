program penjumlahan1_10;
{i.s : diberikan harga pencacah (i) = 10}
{f.s : menampilkan hasil penjumlahan = i + 2 + 3 + .. 10}
var
       hasil, i : integer;


// begin
// writeln('<<<<<<<<<<<<<for do positif>>>>>>>>>>>>>');
// hasil := 0;

// for i := 1 to 10 do
//        hasil := hasil + i;

// write('hasilnya', '', hasil);
// end.



// begin
// writeln('<<<<<<<<<<<<<for do negatif>>>>>>>>>>>>>'); 
// hasil := 0;

// for i := 10 downto 1 do
//        hasil := hasil + i;

// write('hasilnya :', hasil);
// end.



begin
writeln('<<<<<<<<<<<<<while do>>>>>>>>>>>>>'); 
hasil := 0;
i := 1;

begin
while (i <= 10) do
hasil := hasil + i;
i := i + 1;
write('hasilnya :', hasil);
end.
