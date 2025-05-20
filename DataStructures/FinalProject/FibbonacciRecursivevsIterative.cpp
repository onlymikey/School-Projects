#include <iostream>
using namespace std;

// Versión recursiva simple
int fibonacciRecursive(int n) {
    if (n <= 1)
        return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Versión iterativa
int fibonacciIterative(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

// Ejemplo de uso
int main() {
    int n = 10;
    cout << "Fibonacci recursivo de " << n << ": " << fibonacciRecursive(n) << endl;
    cout << "Fibonacci iterativo de " << n << ": " << fibonacciIterative(n) << endl;
    return 0;
}
