let fila_columna = 5;
let matriz = Array.from(Array(fila_columna), () => Array(fila_columna).fill(0));

let max_fila = fila_columna - 1;
let max_columna = fila_columna - 1;
let contador = 1;
for (let i = max_fila; i >= 0; i--) {
    matriz[i][i] = contador;
    contador++;
}

for (let i = 0; i <= max_fila; i++) {
    if (matriz[i][max_columna - i] == 0) {
        matriz[i][max_columna - i] = contador;
        contador++;
    }
}

console.log(matriz);
