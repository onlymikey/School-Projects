#include <vector>

using namespace std;

class Solution {
    public:
    static vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans(nums1.size(), -1);
        for (int i = 0; i < nums1.size(); i++) {
            int j = 0;
            while (j < nums2.size() && nums2[j] != nums1[i]) {
                j++;
            }
            if (j + 1 < nums2.size() && nums2[j + 1] > nums1[i]) {
                ans[i] = nums2[j + 1];
            }
        }
        return ans;
    }
};