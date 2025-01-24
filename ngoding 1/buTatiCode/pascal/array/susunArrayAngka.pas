program susunArrayAngka ;
uses crt;

// Konstanta
const
  MaksAngka = 10;

// Tipe Data
type
  ArrayAngka = array[1..MaksAngka] of integer;
var
  Angka: ArrayAngka;
  banyakData, pilihMetode, pilihCara, pilihSeleksi : integer;

//subrutin menu penggurutan 
procedure menuMetode(var pilihMetode: integer);
begin
  writeln('<<<<<<<< MENU >>>>>>>>');
  writeln('1.buble short');
  writeln('2. selection short');
  writeln('0. KELUAR');
  write('Pilihan Anda: ');
  readln(pilihMetode);
end;

//subrutin cara
procedure menuCara(var pilihCara: integer);
begin
  writeln('<<<<<<<< MENU CARA PENGURUTAN >>>>>>>>');
  writeln('1.ascending');
  writeln('2. descending');
  writeln('0. KELUAR');
  write('Pilihan Anda: ');
  readln(pilihCara);
end;

//MENU METODE SELECTION SHORT
procedure menuSeleksi(var pilihSeleksi: integer);
begin
  writeln('<<<<<<<< MENU SELECTION SHORT>>>>>>>>');
  writeln('1.max short');
  writeln('2. min short');
  writeln('0. KELUAR');
  write('Pilihan Anda: ');
  readln(pilihSeleksi);
end;

procedure PenciptaanAngka(var Angka: ArrayAngka);
var
  i: integer;
begin
  for i := 1 to MaksAngka do
    Angka[i] := 0;
end;

//subrutin memasukan elemen array angka

procedure IsiAngka(Angka: ArrayAngka; BanyakData: integer);
var
  i: integer;
begin
  //memasukan banyak data yang di olah
  write('banyak data yang di olah : '); readln(BanyakData);
  clrscr;
  writeln('<<pengisian array angka sebanyak ',BanyakData,'elemen>>' );
  for i := 1 to BanyakData do
  begin
    write('angka ke-', i,' = '); readln(Angka[i]);
  end;
end;

// Prosedur Tampil Angka
procedure TampilAngka(Angka: ArrayAngka; BanyakData: integer);
var
  i: integer;
begin
  textcolor(12); write('array angka : ');
  textcolor(15); write('| ');
  for i := 1 to BanyakData do
    write(Angka[i] , '|');

  writeln;
end;

//subrutin mengurutkan elem array angka secara ascending
procedure SusunBubbleAsc(var Angka : ArrayAngka; BanyakData : integer);
{is : elemen array angka sudah terdefenisi}
{fs : menghasilkan array angka yang sudah terurut secara ascending menggunakan metode b8ubble short}

var
       i,j,temp : integer;

begin
       for i := 1 to BanyakData - 1 do
              for j := BanyakData downto i+1 do
              begin
                     if (Angka[j] < Angka[j-1])
                     then
                     begin
                            temp := Angka[j];
                            Angka[j] := Angka[j-i];
                            Angka[j-i] := temp;
                     end;
              end;//endfor      
end; //endpro
procedure SusunBubbleDsc(var Angka : ArrayAngka; BanyakData : integer);
{is : elemen array angka sudah terdefenisi}
{fs : menghasilkan array angka yang sudah terurut secara ascending menggunakan metode b8ubble short}

var
       i,j,temp : integer;

begin
       for i := 1 to BanyakData - 1 do
              for j := 1 to BanyakData - i do
              begin
                     if (Angka[j] < Angka[j+1])
                     then
                     begin
                            temp := Angka[j];
                            Angka[j] := Angka[j+i];
                            Angka[j+i] := temp;
                     end;
              end;//endfor      
end; //endpro

begin
       textcolor(15);
       menuMetode(pilihMetode);
       PenciptaanAngka(Angka);
       while (pilihMetode <> 0) do 
       begin
              clrscr;
              case (pilihMetode) of
                     1 :    begin //metode bubble short
                                   textcolor(15);
                                   menuCara(pilihCara);    
                                   while (pilihCara <> 0) do
                                   begin
                                          clrscr;
                                          case (pilihCara) of 
                                                 1 :    begin
                                                        textcolor(yellow); gotoxy(44, 1);
                                                        writeln('<<metode buble shotrt ascending>>');
                                                        IsiAngka(Angka, BanyakData);
                                                        clrscr;
                                                        textcolor(yellow); gotoxy(44, 1);
                                                        writeln('<<metode buble shotrt ascending>>');
                                                        textcolor(11);
                                                        writeln('data sebelu terurut');
                                                        writeln('-------------------');
                                                        TampilAngka(Angka, MaksAngka);

                                                        textcolor(11);writeln();
                                                        writeln('data setelah terurut');
                                                        writeln('-------------------');
                                                        SusunBubbleAsc(Angka,BanyakData);
                                                        TampilAngka(Angka, MaksAngka);
                                                        end;
                                                 2 :    begin
                                                        textcolor(yellow); gotoxy(44, 1);
                                                        writeln('<<metode buble shotrt descending>>');
                                                        IsiAngka(Angka, BanyakData);
                                                        textcolor(11);
                                                        writeln('data sebelu terurut');
                                                        writeln('-------------------');
                                                        TampilAngka(Angka, BanyakData);

                                                        textcolor(11);writeln();
                                                        writeln('data setelah terurut');
                                                        writeln('-------------------');
                                                        SusunBubbleDsc(Angka,BanyakData);
                                                        TampilAngka(Angka, MaksAngka);
                                                        end;
                                          end; //endcase pilih cara
                                          writeln;
                                          writeln('tekan enter kembali ke menu cara pengurutan');
                                          readln;
                                          clrscr;
                                          textcolor(15);
                                          menuCara(pilihCara);
                                   end;//endwhile pilih cara
                            end;
                     2 :    begin //metode seletions short
                                   writeln('<<Metode selektion short>>')
                                   menuSeleksi(pilihSeleksi);
                                   while (pilihSeleksi <> 0) do
                                   begin
                                          clrscr;
                                          case (pilihSeleksi) of
                                          1 :    begin
                                                        menuCara(pilihCara);
                                                        while (pilihCara <> 0);
                                                        begin
                                                               
                                                        end;
                                                 end;
                                          menuSeleksi(pilihSeleksi)
                                   end;
                            end;
                     
              end;//endcase pilih metode
              clrscr;
              textcolor(15);
              menuMetode(pilihMetode);
       end;//endwhile metode
end.