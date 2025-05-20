#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;

    Node(int v) : value(v), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int value) {
    if (!root) return new Node(value);
    if (value < root->value)
        root->left = insert(root->left, value);
    else if (value > root->value)
        root->right = insert(root->right, value);
    return root;
}

bool search(Node* root, int value) {
    if (!root) return false;
    if (root->value == value) return true;
    if (value < root->value)
        return search(root->left, value);
    else
        return search(root->right, value);
}

int main() {
    Node* root = nullptr;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    insert(root, 60);
    insert(root, 80);

    int target = 60;
    cout << "¿Existe " << target << " en el BST? " << (search(root, target) ? "Sí" : "No") << endl;

    return 0;
}
