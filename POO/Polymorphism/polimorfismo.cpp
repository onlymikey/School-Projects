#include <iostream>
using namespace std;

//---------------------------------------------------------------------------------------
// Clase padre
class Vehiculo {
private:
    string marca;
    string modelo;

public:
    Vehiculo(string, string);
    virtual void Mostrar(); // Método virtual para permitir el polimorfismo
};

Vehiculo::Vehiculo(string _marca, string _modelo) {
    marca = _marca;
    modelo = _modelo;
}

void Vehiculo::Mostrar() {
    cout << "Marca: " << marca << endl;
    cout << "Modelo: " << modelo << endl;
}
//---------------------------------------------------------------------------------------
// Sub clase 1
class Automovil : public Vehiculo {
private:
    int numeroPuertas;

public:
    Automovil(string, string, int);
    void Mostrar(); // Polimorfismo de la super clase Mostrar
};

Automovil::Automovil(string _marca, string _modelo, int _numeroPuertas) 
    : Vehiculo(_marca, _modelo) {
    numeroPuertas = _numeroPuertas;
}

void Automovil::Mostrar() {
    Vehiculo::Mostrar(); // Llamada al método de la superclase
    cout << "Número de puertas: " << numeroPuertas << endl;
}
//---------------------------------------------------------------------------------------
// Sub clase 2
class Motocicleta : public Vehiculo {
private:
    string tipo;

public:
    Motocicleta(string, string, string);
    void Mostrar();
};

Motocicleta::Motocicleta(string _marca, string _modelo, string _tipo) 
    : Vehiculo(_marca, _modelo) {
    tipo = _tipo;
}

void Motocicleta::Mostrar() {
    Vehiculo::Mostrar(); // Llamada al método de la superclase
    cout << "Tipo: " << tipo << endl;
}

//---------------------------------------------------------------------------------------
int main() {
    Vehiculo* vector[3];

    vector[0] = new Automovil("Toyota", "Corolla", 4);
    vector[1] = new Motocicleta("Harley-Davidson", "Sportster", "Cruiser");
    vector[2] = new Automovil("Honda", "Civic", 4);

    vector[0]->Mostrar();
    cout << "\n";
    vector[1]->Mostrar();
    cout << "\n";
    vector[2]->Mostrar();
    cout << "\n";

    // Liberar memoria
    for (int i = 0; i < 3; i++) {
        delete vector[i];
    }

    return 0;
}
