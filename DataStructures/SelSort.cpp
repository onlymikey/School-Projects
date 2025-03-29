#include <bits/stdc++.h>

using namespace std;

void SelectionSort(vector<int> &arr) {
	int n = arr.size();
	for(int i = 0; i < n - 1; i++) {

		int min = i;

		for(int j = i + 1; j < n; j++) {
			if(arr[j] < arr[min]) {
				min = j;
			}

		}
		swap(arr[i], arr[min]);
	}
}

void PrintArray(vector<int> &arr) {
	for(int i = 0; i < arr.size(); i++) {
		cout<<arr[i] << " ";
	}
	cout<< endl;
}

int main() {
	vector<int> arr = {6, 8, 0, 1, 4, 9, 1};
	PrintArray(arr);
	SelectionSort(arr);
	PrintArray(arr);

	return 0;
}