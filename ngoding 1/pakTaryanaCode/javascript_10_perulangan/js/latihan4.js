var saldoAwal = 1000000

for (i = 1; i <=12; i++){
       var bunga = 0.05 * saldoAwal
       var saldoAkhir = saldoAwal + bunga
      document.write(
       `
       <tr>
              <td>${i}</td>
              <td>${Math.round(saldoAwal)}</td>
              <td>${Math.round(bunga)}</td>
              <td>${Math.round(saldoAkhir)}</td>
          
       </tr>
       `
) 
var saldoAwal = saldoAkhir
}