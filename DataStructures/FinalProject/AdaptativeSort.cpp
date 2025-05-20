#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> leftPart(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> rightPart(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;
    while (i < leftPart.size() && j < rightPart.size()) {
        if (leftPart[i] <= rightPart[j])
            arr[k++] = leftPart[i++];
        else
            arr[k++] = rightPart[j++];
    }

    while (i < leftPart.size()) arr[k++] = leftPart[i++];
    while (j < rightPart.size()) arr[k++] = rightPart[j++];
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = (left + right) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

void adaptiveSort(vector<int>& arr) {
    int n = arr.size();
    int ordered = 0;
    for (int i = 1; i < n; i++)
        if (arr[i] >= arr[i - 1])
            ordered++;

    double percentageOrdered = double(ordered) / (n - 1);
    if (percentageOrdered >= 0.9)
        insertionSort(arr);
    else
        mergeSort(arr, 0, n - 1);
}

// Ejemplo de uso
int main() {
    vector<int> arr = {1, 2, 3, 8, 5, 6, 7, 4, 9};

    adaptiveSort(arr);

    cout << "Arreglo ordenado: ";
    for (int num : arr)
        cout << num << " ";
    cout << endl;

    return 0;
}
