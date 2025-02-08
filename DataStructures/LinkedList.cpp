#include <iostream>

using namespace std;

class Vertex {
public:
    string data;
    Vertex *next;
    Vertex(string valor) {
        data = valor;
        next = nullptr;
    }
};

class LinkedList {
  public:
    Vertex *head, *tail;
    void append(string valor);
    void InsertHead(string valor);
    void SelectedInsert(string valor, int pos);
    void DeleteTail();
    void DeleteHead();
        void print();
        LinkedList() {
            head = tail = nullptr;
        }
        };

        void LinkedList::append(string valor) {
            Vertex *vtx = new Vertex(valor);
            if (head == nullptr) {
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
            if (tail == nullptr)
                tail = head;
        }

        void LinkedList::DeleteTail() {
            //Deletes first element of the list
            //Check if empty list
            if(head ==  nullptr)  {
                cout<<"Already empty";
                return;
            }
            Vertex *temp;
            temp = tail;
            tail = temp->next;
            delete temp;
        }

        void LinkedList::DeleteHead(){
            //Deletes first element of the list
            //Check if empty list
            if(head ==  nullptr)  {
                cout<<"Already empty";
                return;
            }
            Vertex *temp;
            temp = head;
            head = temp->next;
            delete temp;
            //Consider if only one element
            if(head == nullptr)
                tail = nullptr;
        }

        void LinkedList::SelectedInsert(string valor, int pos) {
            Vertex *vtx = new Vertex(valor);
            if (pos == 0 || head == nullptr) {
                cout<<"Insertando en el inicio de la lista..."<<endl;
                InsertHead(valor);
            }
            else if (pos < 0) {
                cout << "Posicion no valida" << endl;
            }
            else {
                Vertex *temp = head;
                for (int i = 0; i < pos - 1; i++) {
                    temp = temp->next;
                    if (temp == nullptr) {
                        cout << "Posicion no valida" << endl;
                        return;
                    }
                }
                vtx->next = temp->next;
                temp->next = vtx;
                if (vtx->next == nullptr)
                    tail = vtx;
            }
        }

void LinkedList::print() {
    Vertex *temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    LinkedList lista;
            int pos;
            string valor;
            lista.InsertHead("Hola");
            lista.InsertHead("xd");
            lista.InsertHead("omaiga");
            lista.InsertHead("america ya :D");
            lista.InsertHead("Hallo");

                cout << "Elemento: ";
                cin >> valor;
                cout << "Posicion: ";
                cin >> pos;
                lista.SelectedInsert(valor, pos);
            lista.print();
            // lista.DeleteHead();
           lista.DeleteTail();
            lista.print();
            return 0;
}