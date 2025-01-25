#include <iostream>
using namespace std;

bool isPalindrome(string str) {
    int start = 0;
    int end = str.length() - 1;

    while (start < end) {
        if (str[start] != str[end]) {
            return false;
        }

        start++;
        end--;
    }

    return true;
}

int main() {
    string str;
    cout << "Escribe un string: ";
    cin >> str;
    isPalindrome(str) ? cout << "Es palindromo" : cout << "No es palindromo";

}