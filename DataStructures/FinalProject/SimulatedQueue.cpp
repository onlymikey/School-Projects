#include <iostream>
#include <stack>
using namespace std;

class QueueWithStacks {
    stack<int> inStack, outStack;

    void transfer() {
        while (!inStack.empty()) {
            outStack.push(inStack.top());
            inStack.pop();
        }
    }

public:
    void enqueue(int x) {
        inStack.push(x);
    }

    void dequeue() {
        if (outStack.empty()) {
            transfer();
        }
        if (!outStack.empty()) {
            outStack.pop();
        }
    }

    int front() {
        if (outStack.empty()) {
            transfer();
        }
        if (!outStack.empty()) {
            return outStack.top();
        }
        return -1;
    }

    bool empty() {
        return inStack.empty() && outStack.empty();
    }
};

// Ejemplo de uso
int main() {
    QueueWithStacks q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Front: " << q.front() << endl; // 10
    q.dequeue();

    cout << "Front después de dequeue: " << q.front() << endl; // 20

    q.enqueue(40);
    q.dequeue();

    cout << "Front actual: " << q.front() << endl; // 30

    return 0;
}
