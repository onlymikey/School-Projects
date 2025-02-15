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
    void InsertHead(string valor);
    void SelectedInsert(string valor, int pos);
    void deleteHead();
    void deleteTail();
    void InvertList();
    void deleteAt(int pos);
        void print();
        LinkedList() {
            head = tail = NULL;
        }
        };

        void LinkedList::deleteHead() {
            if (head == NULL) {
                cout << "Lista vacia" << endl;
            } else {
                Vertex *temp = head;
                head = head->next;
                delete temp;
                if (head == NULL)
                    tail = NULL;
            }
        }

        void LinkedList::InvertList() {
            Vertex *prev = nullptr;
            Vertex *cur = head;
            Vertex *next = nullptr;
            Vertex *temp = head;

            while (cur != nullptr) {
                next = cur->next;
                cur->next = prev;
                prev = cur;
                cur = next;
            }
            head = prev;
            tail = temp;


        }


        void LinkedList::deleteTail() {
            if (head == NULL) {
                cout << "Lista vacia" << endl;
            } else {
                if (head == tail) {
                    delete head;
                    head = tail = NULL;
                } else {
                    Vertex *temp = head;
                    while (temp->next != tail) {
                        temp = temp->next;
                    }
                    delete tail;
                    tail = temp;
                    tail->next = NULL;
                }
            }
        }

        void LinkedList::deleteAt(int pos) {
            if (head == NULL) {
                cout << "Lista vacia" << endl;
            } else if (pos == 0) {
                deleteHead();
            } else {
                Vertex *temp = head;
                for (int i = 0; i < pos - 1; i++) {
                    temp = temp->next;
                    if (temp == NULL) {
                        cout << "Posicion no valida" << endl;
                        return;
                    }
                }
                Vertex *temp2 = temp->next;
                temp->next = temp2->next;
                delete temp2;
                if (temp->next == NULL)
                    tail = temp;
            }
        }


        void LinkedList::append(string valor) {
            Vertex *vtx = new Vertex(valor);
            if (head == NULL) {
                head = tail = vtx;
            } else {
                tail->next = vtx;
                tail = vtx;
            }
        }

        void LinkedList::InsertHead(string valor) {
            Vertex *vtx = new Vertex(valor);
            vtx->next = head;
            head = vtx;
            if (tail == NULL)
                tail = head;
        }

        void LinkedList::SelectedInsert(string valor, int pos) {
            Vertex *vtx = new Vertex(valor);
            if (pos == 0) {
                InsertHead(valor);
            }
            else if (pos < 0) {
                cout << "Posicion no valida" << endl;
            }
            else {
                Vertex *temp = head;
                for (int i = 0; i < pos - 1; i++) {
                    temp = temp->next;
                    if (temp == NULL) {
                        cout << "Posicion no valida" << endl;
                        return;
                    }
                }
                vtx->next = temp->next;
                temp->next = vtx;
                if (vtx->next == NULL)
                    tail = vtx;
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

int main() {
    LinkedList lista;
            int pos;
            string valor;
            lista.print();
            lista.append("1");
            lista.print();
            lista.append("2");
            lista.print();
            lista.append("3");
            lista.print();
            lista.append("4");
            lista.print();
            lista.append("5");
            lista.print();
            lista.InvertList();
    lista.print();
}