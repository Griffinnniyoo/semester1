
for (i = 1; i<= 10; i ++){
       hargaAwalJeruk = 8000
       hargaAwalMangga = 10000
       document.write(
              `
              
              <tr>
                     <td>${i}</td> 
                     <td>${hargaAwalJeruk * i}</td> 
                     <td>${hargaAwalMangga * i}</td> 
              </tr>
              
              `
       )
}