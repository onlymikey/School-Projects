#include <iostream>
#include <string>

using namespace std;

class Vertex {
public:
    string data;
    Vertex *next;
    Vertex *prev;
    explicit Vertex(const string &valor) {
        data = valor;
        next = nullptr;
        prev = nullptr;
    }
};

class LinkedList {
public:
    Vertex *head, *tail;
    LinkedList() : head(nullptr), tail(nullptr) {}
    void append(const string& valor);
    void InsertHead(const string& valor);
    void SelectedInsert(const string& valor, int pos);
    void deleteHead();
    void deleteTail();
    void deleteAt(int pos);
    void InvertList();
    void CompareList(LinkedList lista, LinkedList lista2);
    void print() const;
};

void LinkedList::append(const string& valor) {
    Vertex *vtx = new Vertex(valor);
    if (head == nullptr) {
        head = tail = vtx;
    } else {
        tail->next = vtx;
        vtx->prev = tail;
        tail = vtx;
    }
}

void LinkedList::InsertHead(const string& valor) {
    Vertex *vtx = new Vertex(valor);
    if (head == nullptr) {
        head = tail = vtx;
    } else {
        vtx->next = head;
        head->prev = vtx;
        head = vtx;
    }
}

void LinkedList::SelectedInsert(const string& valor, int pos) {
    if (pos == 0) {
        InsertHead(valor);
    } else {
        Vertex *temp = head;
        for (int i = 0; i < pos - 1; i++) {
            temp = temp->next;
            if (temp == nullptr) {
                cout << "Posicion no valida" << endl;
                return;
            }
        }
        Vertex *vtx = new Vertex(valor);
        vtx->next = temp->next;
        vtx->prev = temp;
        if (temp->next != nullptr) {
            temp->next->prev = vtx;
        }
        temp->next = vtx;
        if (vtx->next == nullptr) {
            tail = vtx;
        }
    }
}

void LinkedList::deleteHead() {
    if (head == nullptr) {
        cout << "Lista vacia" << endl;
    } else {
        Vertex *temp = head;
        head = head->next;
        if (head != nullptr) {
            head->prev = nullptr;
        } else {
            tail = nullptr;
        }
        delete temp;
    }
}

void LinkedList::deleteTail() {
    if (tail == nullptr) {
        cout << "Lista vacia" << endl;
    } else {
        Vertex *temp = tail;
        tail = tail->prev;
        if (tail != nullptr) {
            tail->next = nullptr;
        } else {
            head = nullptr;
        }
        delete temp;
    }
}

void LinkedList::deleteAt(int pos) {
    if (head == nullptr) {
        cout << "Lista vacia" << endl;
    } else if (pos == 0) {
        deleteHead();
    } else {
        Vertex *temp = head;
        for (int i = 0; i < pos; i++) {
            temp = temp->next;
            if (temp == nullptr) {
                cout << "Posicion no valida" << endl;
                return;
            }
        }
        temp->prev->next = temp->next;
        if (temp->next != nullptr) {
            temp->next->prev = temp->prev;
        } else {
            tail = temp->prev;
        }
        delete temp;
    }
}

void LinkedList::InvertList() {
    Vertex *temp = nullptr;
    Vertex *current = head;
    while (current != nullptr) {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev;
    }
    if (temp != nullptr) {
        head = temp->prev;
    }
}

void LinkedList::CompareList(LinkedList lista, LinkedList lista2) {
    Vertex *ls1 = lista.head;
    Vertex *ls2 = lista2.head;
    while (ls1 != nullptr && ls2 != nullptr) {
        if (ls1->data == ls2->data) {
            cout << ls1->data << " ";
        }
        ls1 = ls1->next;
        ls2 = ls2->next;
    }
    cout << endl;
}

void LinkedList::print() const {
    Vertex *temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    LinkedList lista;
    lista.append("7");
    lista.append("8");
    lista.append("3");
    lista.append("4");
    lista.append("9");
    lista.print();

    LinkedList lista2;
    lista2.append("1");
    lista2.append("2");
    lista2.append("3");
    lista2.append("4");
    lista2.append("5");
    lista2.print();

    lista.CompareList(lista, lista2);

    return 0;
}