let filas = 5;
let columnas = 5;
let matriz = Array.from(Array(filas), () => Array(columnas).fill(0));

function impresion(matriz){
    for(let i= 0; i < matriz.length; i++ ){
        let fila = matriz[i].join("\t");
        console.log(fila);
    }
}


let inicio = 1;
//recorre filas
for(let i=0; i< matriz.length; i++){
    let reemplazo = inicio
    //recoore columnas
    for(let j=0; j< matriz[0].length; j++){
        matriz[i][j] = reemplazo
        reemplazo= reemplazo + filas
    }
    inicio++;
}


let matriz1 = Array.from(Array(filas), () => Array(columnas).fill(0));

fila_max = filas-1;
columna_max = columnas-1;
fila_min = 4;
columna_min = 0;
contador = 1;
for (let i = columna_max; i >= columna_min; i--) {
    matriz[fila_max][i] = contador++;
}
fila_max--;

  
   

impresion(matriz1)
//impresion(matriz);
