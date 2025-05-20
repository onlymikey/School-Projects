#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

void convertToCumulativeSum(Node* head) {
    int cumulative = 0;
    Node* current = head;
    while (current != nullptr) {
        cumulative += current->data;
        current->data = cumulative;
        current = current->next;
    }
}

void printList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        cout << current->data;
        if (current->next) cout << " -> ";
        current = current->next;
    }
    cout << endl;
}

// Ejemplo de uso
int main() {
    Node* head = new Node(1);
    head->next = new Node(3);
    head->next->next = new Node(5);
    head->next->next->next = new Node(7);

    cout << "Lista original: ";
    printList(head);

    convertToCumulativeSum(head);

    cout << "Lista transformada: ";
    printList(head);

    return 0;
}
