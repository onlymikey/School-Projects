#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1; // Índice del elemento más pequeño

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1; // Retorna la posición del pivote
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Ordenar la parte izquierda
        quickSort(arr, pi + 1, high); // Ordenar la parte derecha
    }
}

// Ejemplo de uso
int main() {
    vector<int> arr = {8, 4, 2, 9, 1, 5, 3, 7, 6};

    quickSort(arr, 0, arr.size() - 1);

    cout << "Arreglo ordenado con QuickSort: ";
    for (int num : arr)
        cout << num << " ";
    cout << endl;

    return 0;
}
