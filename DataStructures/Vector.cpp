#include <iostream>
#include <vector>
using namespace std;

int main()
{
  // v1 es un vector de 5 elementos enteros con valor 0
  vector<int> v1(5);
  cout << "Número de elementos de v1: " << v1.size() << endl;
  // v2 es un vector de 1 elemento entero con valor 5
  vector<int> v2{5};
  cout << "Número de elementos de v2: " << v2.size() << endl;
  // v3 es un vector de 5 elementos enteros inicializados a 1
  vector<int> v3(5, 1);
  cout << "Elementos de v3:\n";
  for (int i = 0 ; i != v3.size(); ++i)
    cout << v3[i] << endl;
  // v4 es un vector de 2 elementos enteros con valores 5 y 1
  vector<int> v4{5, 1};
  cout << "Elementos de v4:\n";
  for (int i = 0 ; i < v4.size(); ++i)
    cout << v4[i] << endl;
  // v5 es un vector incializado con los valores de v4
  vector<int> v5(v4);
  cout << "Elementos de v5:\n";
  for (int i = 0 ; i < v5.size(); ++i)
    cout << v5[i] << endl;
}
