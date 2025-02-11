#include <iostream>
using namespace std;
class Vertex{
public:
    int data;
    Vertex *next;
    Vertex(int data){
        this->data = data;
        next = nullptr;
    }
};
class LL{
private:
    Vertex *head,*tail;
public:
    LL(){ head = tail = nullptr;}
    void insertHead(int data);
    void insertTail(int data);
    void deleteHead();
    void print();
};
void LL::print(){
    //Print all elements of the list
    //To consider: Prints until nullptr or tail
    // To Do: what if its empty?
    if(head == nullptr){
        cout<<"Empty list"<<endl;
        return;
    }
    Vertex *temp = head;
    while(temp != nullptr){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
    cout<<endl;
}
void LL::insertHead(int data){
    //Inserts an element at the head
    //To Do: if empty update tail
    Vertex *vtx = new Vertex(data);
    vtx->next = head;
    head = vtx;
    if(tail == nullptr)
        tail = head;
}
void LL::insertTail(int data){
    //Insert element at the end
    Vertex *vtx = new Vertex(data);
    if(tail != nullptr)
        tail->next = vtx;
    tail = vtx;
    //Check if its empty
    if(head == nullptr)
        head = tail;
}
void LL::deleteHead(){
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
int main() {
    LL lista;
    lista.print();
    lista.insertTail(1);
    lista.print();
    lista.deleteHead();
    lista.print();
    lista.insertTail(10);
    lista.print();
    lista.insertHead(5);
    lista.print();
    lista.insertHead(7);
    lista.print();
    lista.insertHead(2);
    lista.print();
    lista.insertTail(10);
    lista.print();

}