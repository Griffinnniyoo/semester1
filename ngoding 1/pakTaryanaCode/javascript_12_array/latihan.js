let namaSiswa = ['RIJAL', 'GIO', 'TEGAR', 'FADIL', 'SULTAN', 'VANO', 'JAWA']
let matkul = ['WEB 1', 'LOGMAT', 'MSD', 'LOGIKA SAINS DATA', 'INDONESIA', 'INGGRIS', 'PSTI']
let tugas = [70,80,80,70,90,80,70]
let uts = [90,80,70,90,80,70,80]
let uas = [70,90,90,60,70,80,90]

nilaiAkhir = 0
grade = ""

for (i = 0; i < namaSiswa.length; i++){
       nilaiAkhir = (0.2 * tugas[i]) + (0.3 * uts[i]) + (0.5 * uas[i])
       if (nilaiAkhir >= 80){
              grade = 'A'
       } else {
              if (nilaiAkhir >= 70) {
                     grade = 'B'
              } else { 
                     if (nilaiAkhir >= 60){
                            grade = 'C'
                     } else {
                            if (nilaiAkhir >= 50){
                                   grade = 'D'
                            }else {
                                   if (nilaiAkhir <= 50){
                                          grade = 'E'
                                   }
                            }
                     }
              }
       }
       
       
      
       document.write(
              `
                     <tr>
                            <td>${i + 1}</td>
                            <td>${namaSiswa[i]}</td>
                            <td>${matkul[i]}</td>
                            <td align="center">${tugas[i]}</td>
                            <td align="center">${uts[i]}</td>
                            <td align="center">${uas[i]}</td>
                            <td align="center">${nilaiAkhir}</td> 
                            <td align="center">${grade}</td> 
                     </tr>
              `
       )
}