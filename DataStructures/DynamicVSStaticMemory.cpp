#include <iostream>
#include <cstring> // Strcpy
#include <cstdlib> // Dynamic memory

using namespace std;

// Structure
struct Person {
    char name[50];
    int age;
};

// CLass
class Vehicle {
private:
    string brand;
    int model;

public:
    // Constructor
    Vehicle(string b, int m) : brand(b), model(m) {}

    void show() {
        cout << "Vehicle: " << brand << ", Model: " << model << endl;
    }
};

int main() {
    // Variables
    int staticVariable = 42;
    int *dynamicVariable = new int(42);

    cout << "Static variable: " << staticVariable << endl;
    cout << "Dynamic variable: " << *dynamicVariable << endl;

    delete dynamicVariable;

    // Arrays
    int staticArray[5] = {1, 2, 3, 4, 5};
    int *dynamicArray = new int[5]{1, 2, 3, 4, 5};

    cout << "Static array: ";
    for (int i = 0; i < 5; i++) {
        cout << staticArray[i] << " ";
    }
    cout << endl;

    cout << "Dynamic array: ";
    for (int i = 0; i < 5; i++) {
        cout << dynamicArray[i] << " ";
    }
    cout << endl;

    delete[] dynamicArray;

    // Structures
    Person staticPerson;
    strcpy(staticPerson.name, "John");
    staticPerson.age = 25;

    Person *dynamicPerson = (Person *)malloc(sizeof(Person));
    strcpy(dynamicPerson->name, "Anna");
    dynamicPerson->age = 30;

    cout << "Static structure: " << staticPerson.name << ", " << staticPerson.age << endl;
    cout << "Dynamic structure: " << dynamicPerson->name << ", " << dynamicPerson->age << endl;

    free(dynamicPerson);

    // Classes
    Vehicle staticVehicle("Toyota", 2020);
    Vehicle *dynamicVehicle = new Vehicle("Honda", 2021);

    cout << "Static class: ";
    staticVehicle.show();

    cout << "Dynamic class: ";
    dynamicVehicle->show();

    delete dynamicVehicle;

    return 0;
}
