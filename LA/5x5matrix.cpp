#include <iostream>
#include <vector>
using namespace std;

// Función para calcular el determinante de una matriz
int determinant(vector<vector<int>> matrix, int size) {
    int det = 0; // Inicializa el determinante en 0

    // Caso base: si la matriz es de 1x1, regresa el único elemento
    if (size == 1) {
        return matrix[0][0];
    }

    // Caso base: si la matriz es de 2x2, usa la fórmula directa para determinantes
    if (size == 2) {
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]);
    }

    // Bucle para aplicar la expansión por cofactores a lo largo de la primera fila
    for (int p = 0; p < size; p++) {
        vector<vector<int>> subMatrix(size - 1, vector<int>(size - 1)); // Submatriz para expansión por cofactores

        // Crear la submatriz eliminando la primera fila y la columna actual
        for (int i = 1; i < size; i++) {
            int colIndex = 0; // Índice de columna para la submatriz
            for (int j = 0; j < size; j++) {
                if (j != p) { // Saltar la columna que se está expandiendo
                    subMatrix[i - 1][colIndex] = matrix[i][j];
                    colIndex++;
                }
            }
        }

        // Recursivamente calcular el determinante de la submatriz y acumular los resultados
        det += matrix[0][p] * determinant(subMatrix, size - 1) * (p % 2 == 0 ? 1 : -1); // Alternar el signo
    }

    return det;
}

int main() {
    // Definir una matriz de 5x5
    vector<vector<int>> matrix = {
        {3, 2, 1, 5, 7},
        {1, 4, 2, 3, 9},
        {6, 1, 8, 1, 4},
        {7, 9, 4, 6, 2},
        {5, 2, 3, 1, 8}
    };

    // Imprimir el determinante de la matriz 5x5
    cout << "El determinante de la matriz es: " << determinant(matrix, 5) << endl;

    return 0;
}
