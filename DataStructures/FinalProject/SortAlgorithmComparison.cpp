#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int> arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; ++i) {
        for (int j = 0; j < n-i-1; ++j) {
            if (arr[j] > arr[j+1])
                swap(arr[j], arr[j+1]);
        }
    }
    cout << "Bubble Sort: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
}

void selectionSort(vector<int> arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; ++i) {
        int minIdx = i;
        for (int j = i+1; j < n; ++j)
            if (arr[j] < arr[minIdx])
                minIdx = j;
        swap(arr[i], arr[minIdx]);
    }
    cout << "Selection Sort: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low >= high) return;
    int pivot = arr[high];
    int i = low;
    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot)
            swap(arr[i++], arr[j]);
    }
    swap(arr[i], arr[high]);
    quickSort(arr, low, i - 1);
    quickSort(arr, i + 1, high);
}

void printVector(const vector<int>& arr, const string& title) {
    cout << title << ": ";
    for (int num : arr) cout << num << " ";
    cout << endl;
}

int main() {
    vector<int> data = {8, 2, 5, 1, 9, 4, 7, 6, 3};

    bubbleSort(data);
    selectionSort(data);

    vector<int> quick = data;
    quickSort(quick, 0, quick.size() - 1);
    printVector(quick, "QuickSort");

    return 0;
}
