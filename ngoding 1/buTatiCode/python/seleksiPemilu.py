# I.S {user input umur}
# F.S {output bole ikut pemilu atau tidak}


# badanProgam
umur = int(input('masukan umur anda :'))
print('---------------------------------')

if umur < 17 :
       menikah = str(input('menikah [Y/T] ? :')).upper()
       # if menikah == 'Y':
              # print('---------------------------------')
              # print('anda boleh ikut pemilu')
       # else :
       #        print('---------------------------------')
       #        print('anda belum boleh ikut pemilu')

       #menyederhakan bentuk if
       match (menikah):
              case 'Y':
                     print('anda boleh ikut pemilu')
              case 'T':
                     print('anda ga boleh ikut pemilu')
              case _ : 
                     print('hanya bisa [Y/T]')

else :
       print('---------------------------------')
       print('anda boleh ikut pemilu')