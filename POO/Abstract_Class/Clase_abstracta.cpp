#include <iostream>
#include <string>
using namespace std;

// Clase padre Herramientas
class Herramientas {
protected:
    string nombre;
    double precio;
    string color;

public:
    Herramientas(string nombre, double precio, string color) {
        this->nombre = nombre;
        this->precio = precio;
        this->color = color;
    }

    void cambiar_precio(double nuevo_precio) {
        precio = nuevo_precio;
    }

    void cambiar_color(string nuevo_color) {
        color = nuevo_color;
    }

    void imprimir_datos() const {
        cout << "Herramienta: " << nombre << endl;
        cout << "Precio: $" << precio << endl;
        cout << "Color: " << color << endl;
    }
};

// Clase hija HerramientasPlomero
class HerramientasPlomero : public Herramientas {
public:
    HerramientasPlomero(string nombre, double precio, string color)
        : Herramientas(nombre, precio, color) {}
};

// Clase hija HerramientasCarpintero
class HerramientasCarpintero : public Herramientas {
public:
    HerramientasCarpintero(string nombre, double precio, string color)
        : Herramientas(nombre, precio, color) {}
};

int main() {
    // Creación de los objetos Soldadora y Serrucho
    HerramientasPlomero soldadora("Soldadora", 1500.0, "Negro");
    HerramientasCarpintero serrucho("Serrucho", 500.0, "Marrón");

    // Imprimir los datos actuales antes de los cambios
    cout << "Datos actuales de la Soldadora:" << endl;
    soldadora.imprimir_datos();

    cout << "\nDatos actuales del Serrucho:" << endl;
    serrucho.imprimir_datos();

    // Cambiar el precio del objeto Soldadora
    double nuevo_precio_soldadora;
    cout << "\nIntroduce el nuevo precio para la Soldadora: ";
    cin >> nuevo_precio_soldadora;
    soldadora.cambiar_precio(nuevo_precio_soldadora);

    // Cambiar el color del objeto Serrucho
    string nuevo_color_serrucho;
    cout << "Introduce el nuevo color para el Serrucho: ";
    cin >> nuevo_color_serrucho;
    serrucho.cambiar_color(nuevo_color_serrucho);

    // Imprimir los datos de los objetos modificados
    cout << "\nDatos modificados de la Soldadora:" << endl;
    soldadora.imprimir_datos();

    cout << "\nDatos modificados del Serrucho:" << endl;
    serrucho.imprimir_datos();

    return 0;
}
