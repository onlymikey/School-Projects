#include <iostream>
#include <string>

using namespace std;

class Vertex {
public:
    string data;
    Vertex *next;
    explicit Vertex(const string &valor) {
        data = valor;
        next = nullptr;
    }
};

class LinkedList {
public:
    Vertex *head, *tail;
    LinkedList() : head(nullptr), tail(nullptr) {}
    void enqueue(const string& valor);
    void enqueue(long long valor);
    void dequeue();
    void back() const;
    void front() const;
    void print() const;
};

void LinkedList::enqueue(const string& valor) {
    if (valor.empty()) {
        cout<<("Input invalido, se esperaba un string no vacío") <<endl;
        return;
    }
    try {
        Vertex *vtx = new Vertex(valor);
        if (head == nullptr) {
            head = tail = vtx;
        } else {
            tail->next = vtx;
            tail = vtx;
        }
    } catch (const bad_alloc&) {
        cout << "Error de asignación de memoria" << endl;
    }
}

void LinkedList::enqueue(long long valor) {
    enqueue(to_string(valor));
}

void LinkedList::dequeue() {
    if (head == nullptr) {
        cout << "Pila vacia" << endl;
    } else {
        Vertex *temp = head;
        head = head->next;
        delete temp;
        if (head == nullptr)
            tail = nullptr;
    }
}

void LinkedList::back() const {
    if (tail == nullptr) {
        cout << "Pila vacia" << endl;
    } else {
        cout << tail->data << endl;
    }
}

void LinkedList::front() const {
    if (head == nullptr) {
        cout << "Pila vacia" << endl;
    } else {
        cout << head->data << endl;
    }
}

void LinkedList::print() const {
    const Vertex *temp = head;
    if (temp == nullptr) {
        cout << "Pila vacia" << endl;
    } else {
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
}

int main() {
    LinkedList pila{};
    pila.enqueue("");
    pila.enqueue(3);
    pila.print();
    pila.back();
    pila.front();
    pila.dequeue();
    pila.print();
    pila.front();
    pila.back();
    pila.dequeue();
    pila.dequeue();
    pila.print();

    return 0;
}