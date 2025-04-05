#include <iostream>

using namespace std;

int fibonacci_recursive(int n) {
    if (n == 0) {
        return 0;
    }
    if (n <= 1) {
        return n;
    }
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int fibonacci_iterative(int n) {
    if (n <= 1) {
        return n;
    }
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return c;
}


int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    cout << "Fibonacci de " << n << " (recursivo): " << fibonacci_recursive(n) << endl;
    cout << "Fibonacci de " << n << " (iterativo): " << fibonacci_iterative(n) << endl;

    return 0;
}