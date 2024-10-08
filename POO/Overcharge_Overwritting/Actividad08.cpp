#include <iostream>
#include <string>
using namespace std;

//----------------------------------CLASE PADRE----------------------------------

class canasta {
    public:
        // Sobrecarga de métodos
        void QueHay(int a) {
            cout << "Hay una bolsa de " << a << " kilos" << endl;
            cout << "--------------------------------------" << endl;
        }

        void QueHay(int a, int b) {
            cout << "Hay una bolsa de " << a << " kilos" << endl;
            cout << "Y otra bolsa de " << b << " kilos" << endl;
            cout << "--------------------------------------" << endl;
        }

        // Método a sobrescribir
        void QueEs() {
            cout << "Esta es una canasta con objetos desconocidos" << endl;
            cout << "--------------------------------------" << endl << endl << endl;
        }

};

//-------------------------------- CLASES HIJAS --------------------------------

class canasta_fruta : public canasta {  // La clase hija hereda de la clase padre
    public:
        // Sobrescritura del método QueEs
        void QueEs() {
            cout << "Esta es una canasta que contiene frutas" << endl;
            cout << "--------------------------------------" << endl << endl << endl;
        }
};

class canasta_verdura : public canasta {  // La clase hija hereda de la clase padre
    public:
        // Sobrescritura del método QueEs
        void QueEs() {
            cout << "Esta es una canasta que contiene verduras" << endl;
            cout << "--------------------------------------" << endl << endl << endl;
        }
};

//------------------------------------ MAIN ------------------------------------

int main() {

    // Creación de objetos de cada clase
    canasta c_generica;
    canasta_fruta c_frutas;
    canasta_verdura c_verduras;

    // Asignarles sus respectivas cantidades y mostrar el tipo de canasta
    // Canasta genérica
    c_generica.QueEs();
    c_generica.QueHay(5); // Solo una bolsa

    // Canasta de frutas
    c_frutas.QueEs();
    c_frutas.QueHay(3, 7); // Dos bolsas con diferentes cantidades

    // Canasta de verduras
    c_verduras.QueEs();
    c_verduras.QueHay(4); // Solo una bolsa

    return 0;
}
