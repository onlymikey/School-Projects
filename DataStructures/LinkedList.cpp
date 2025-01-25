#include <iostream>

using namespace std;

class Vertex {
public:
    string data;
    Vertex *next;
    Vertex(string valor) {
        data = valor;
        next = NULL;
    }
};

class LinkedList {
  public:
    Vertex *head, *tail;
    void append(string valor);
        void print();
        LinkedList() {
            head = tail = NULL;
        }
        };

        void LinkedList::append(string valor) {
            Vertex *nuevo = new Vertex(valor);
            if (head == NULL) {
                head = tail = nuevo;
            } else {
                tail->next = nuevo;
                tail = nuevo;
            }
        }

void LinkedList::print() {
    Vertex *temp = head;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void InsertHead(Vertex **head, string valor) {
    Vertex *nuevo = new Vertex(valor);
    nuevo->next = *head;
    *head = nuevo;
}

int main() {
    LinkedList lista;
            cout << "Agrega 10 elementos a la lista" << endl;

            for (int i = 0; i < 10; i++) {
                string valor;
                cout << "Elemento " << i + 1 << ": ";
                cin >> valor;
                lista.append(valor);
            }
    lista.print();
}