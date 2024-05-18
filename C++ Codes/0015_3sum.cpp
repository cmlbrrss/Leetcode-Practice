class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] > 0){
                return ans;
            }
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int lIdx = i + 1;
            int rIdx = nums.size() - 1;
            while(lIdx < rIdx){
                if (nums[i] + nums[lIdx] + nums[rIdx] == 0){
                    ans.push_back(vector<int>{nums[i], nums[lIdx], nums[rIdx]});
                    while(lIdx < rIdx && nums[lIdx] == nums[lIdx + 1]){
                        lIdx++;
                    }
                    while(lIdx < rIdx && nums[rIdx] == nums[rIdx - 1]){
                        rIdx--;
                    }
                    lIdx++;
                    rIdx--;
                } else if(nums[i] + nums[lIdx] + nums[rIdx] > 0) {
                    rIdx--;
                } else {
                    lIdx++;
                }
            }
        }
        return ans;
    }
};
