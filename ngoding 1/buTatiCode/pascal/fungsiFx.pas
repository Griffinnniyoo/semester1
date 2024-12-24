program MenghitungFungsiFx;
{I.S : pengguna memasukan harga x}
{F.S : menghasilkan harga x}


//Kamus Global 
var
       x : integer;


procedure IsiX(var x : integer);//byReferenns
{I.S : pengguna memasukan harga x}
{F.S : menghasilkan harga x}
begin
       write('masukan harga x = ');readln(x);
end. //endprocedure

function F(x : integer):integer;
{I.S : harga x sudah terdefinisikan }
{F.S : mengahasilkan fungsi f(x)}
begin
       F := 2 * x + 1;
end.

begin
       
end;

procedure TampilFX( x : integer);//byValue
{I.S : harga x sudah terdefinisikan }
{F.S : menampilkan fungsi f(x)}

begin
       write('F(',X,') = ' = F(x))
end. //endprocedure    


//badanProgramUtama
begin
       writeln('<<PROGRAM MENGHITUNG X>>')
       IsiX(x);
       TampilFX(x);
       readln;
end.