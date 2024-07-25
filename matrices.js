let matriz1_columna1 = 5;
let matriz1 = Array.from(Array(matriz1_columna1), () => Array(matriz1_columna1).fill(0));

let max_fila = matriz1_columna1 - 1;
let max_columna = matriz1_columna1 - 1;
let contador = 1;
for (let i = 1; i >= max_columna; i++) {
    matriz1[i][i] = contador + 5;
    contador++;
}

console.log(matriz1);
