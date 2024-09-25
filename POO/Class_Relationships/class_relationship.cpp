#include <iostream>
#include <string>

using namespace std;

//----------------------------------------------------------------
class Personal {
public:
    // atributos
    int id[2]{};
    string direccion[2];
    int edad[2]{};
    string nombres[2];
    // métodos
    Personal(int[2], string[2], int[2], string[2]);    // constructor
    void mostrarPersonal();
};

Personal::Personal(int _id[2], string _direccion[2], int _edad[2], string _nombres[2]) { // constructor
    for (int i = 0; i < 2; i++) {
        id[i] = _id[i];
        direccion[i] = _direccion[i];
        edad[i] = _edad[i];
        nombres[i] = _nombres[i];
    }
}

void Personal::mostrarPersonal() {
    for (int i = 0; i < 2; i++) {
        cout << "ID: " << id[i] << ", Nombre: " << nombres[i] << ", Dirección: " << direccion[i] << ", Edad: " << edad[i] << endl;
    }
}
//----------------------------------------------------------------

class Cocinero : public Personal {  // La clase hija hereda de la clase padre
public:
    // atributos exclusivos
    string vestimenta[2][2];  // [i][0] for gorroDeChef, [i][1] for delantal
    // métodos
    Cocinero(int[2], string[2], int[2], string[2], string[2], string[2]);  // constructor
    void mostrarPersonal();  // método para mostrar personal incluyendo vestimenta
};

// nuevo constructor utilizando al constructor de la clase padre
Cocinero::Cocinero(int _id[2], string _direccion[2], int _edad[2], string _nombres[2], string _gorroDeChef[2], string _delantal[2])
    : Personal(_id, _direccion, _edad, _nombres) {
    for (int i = 0; i < 2; i++) {
        vestimenta[i][0] = _gorroDeChef[i];
        vestimenta[i][1] = _delantal[i];
    }
}

void Cocinero::mostrarPersonal() {
    cout << "Nuestro personal es:\n";
    for (int i = 0; i < 2; i++) {
        cout << "ID: " << id[i] << ", Nombre: " << nombres[i] << ", Dirección: " << direccion[i] << ", Edad: " << edad[i] << endl;
        cout << "Gorro de Chef: " << vestimenta[i][0] << ", Delantal: " << vestimenta[i][1] << " (Chef)" << endl;
    }
}

int main() {
    int id[2] = {1, 2};
    string direccion[2] = {"Calle Falsa 1", "Calle Falsa 2"};
    int edad[2] = {30, 25};
    string nombres[2] = {"Fabritzio", "Marchello"};
    string gorroDeChef[2] = {"Gorro Blanco", "Gorro Negro"};
    string delantal[2] = {"Delantal Blanco", "Delantal Negro"};
    Cocinero cocinero(id, direccion, edad, nombres, gorroDeChef, delantal);   // crea objeto
    cocinero.mostrarPersonal();   // llama a la función mostrarPersonal
}