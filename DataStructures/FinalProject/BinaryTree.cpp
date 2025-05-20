#include <iostream>
#include <vector>
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
    else
        root->right = insert(root->right, value);
    return root;
}

void inorderTraversal(Node* root, vector<int>& values) {
    if (!root) return;
    inorderTraversal(root->left, values);
    values.push_back(root->value);
    inorderTraversal(root->right, values);
}

Node* buildBalancedTree(const vector<int>& values, int start, int end) {
    if (start > end) return nullptr;
    int mid = (start + end) / 2;
    Node* root = new Node(values[mid]);
    root->left = buildBalancedTree(values, start, mid - 1);
    root->right = buildBalancedTree(values, mid + 1, end);
    return root;
}

Node* rebalanceTree(Node* root) {
    vector<int> values;
    inorderTraversal(root, values);
    return buildBalancedTree(values, 0, values.size() - 1);
}

void printInorder(Node* root) {
    if (!root) return;
    printInorder(root->left);
    cout << root->value << " ";
    printInorder(root->right);
}

int main() {
    Node* root = nullptr;
    for (int i = 1; i <= 10; ++i) {
        root = insert(root, i);  // Inserta en orden creciente, desbalanceado
    }

    cout << "Árbol original (inorden): ";
    printInorder(root);
    cout << endl;

    root = rebalanceTree(root);

    cout << "Árbol re-balanceado (inorden): ";
    printInorder(root);
    cout << endl;

    return 0;
}
