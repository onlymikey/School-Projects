#include <iostream>
#include <stack>
using namespace std;

class SmartStack {
    stack<long long> st;
    long long minVal;

public:
    void push(int x) {
        if (st.empty()) {
            st.push(x);
            minVal = x;
        } else if (x < minVal) {
            st.push(2LL * x - minVal); // codificamos el nuevo mínimo
            minVal = x;
        } else {
            st.push(x);
        }
    }

    void pop() {
        if (st.empty()) return;
        long long top = st.top();
        st.pop();
        if (top < minVal) {
            minVal = 2 * minVal - top; // decodificamos el mínimo anterior
        }
    }

    int top() {
        if (st.empty()) return -1;
        long long top = st.top();
        if (top < minVal) return minVal; // el top era codificado
        return top;
    }

    int getMinAbsolute() {
        return st.empty() ? -1 : minVal;
    }

    int getMinRelative() {
        if (st.size() < 2) return -1;

        long long last = st.top(); st.pop();
        long long second = st.top();
        st.push(last); // restauramos

        int lastVal = (last < minVal) ? minVal : last;
        int secondVal = (second < minVal) ? minVal : second;

        return (secondVal < lastVal) ? secondVal : -1;
    }
};

// Ejemplo de uso
int main() {
    SmartStack s;
    s.push(10);
    s.push(5);
    s.push(7);
    s.push(2);

    cout << "Top: " << s.top() << endl;
    cout << "Min absoluto: " << s.getMinAbsolute() << endl;
    cout << "Min relativo: " << s.getMinRelative() << endl;

    s.pop();
    cout << "Después de pop:\n";
    cout << "Top: " << s.top() << endl;
    cout << "Min absoluto: " << s.getMinAbsolute() << endl;

    return 0;
}
