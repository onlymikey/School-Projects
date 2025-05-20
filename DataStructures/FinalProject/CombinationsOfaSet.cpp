#include <iostream>
#include <vector>
using namespace std;

void generateCombinations(const vector<int>& nums, int index, vector<int>& current, vector<vector<int>>& result) {
    if (index == nums.size()) {
        result.push_back(current);
        return;
    }

    // Excluir el elemento actual
    generateCombinations(nums, index + 1, current, result);

    // Incluir el elemento actual
    current.push_back(nums[index]);
    generateCombinations(nums, index + 1, current, result);
    current.pop_back(); // backtrack
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result;
    vector<int> current;

    generateCombinations(nums, 0, current, result);

    cout << "Combinaciones posibles:" << endl;
    for (const auto& combination : result) {
        cout << "{ ";
        for (int num : combination)
            cout << num << " ";
        cout << "}" << endl;
    }

    return 0;
}
