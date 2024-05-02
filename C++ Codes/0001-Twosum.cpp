/* 最快解答 */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mp; //使用哈希表的搜尋法
        int n=nums.size();
        vector<int>ans;
        for(int i=0;i<n;i++){            
            if(mp.find(target-nums[i])!=mp.end()){  // if mp中有找到target-nums[i]。若mp.find()查無target-nums[i]的key則會返回mp.end()
                ans.push_back(mp[target-nums[i]]);  // insert mp[target-nums[i]] to ans
                ans.push_back(i); // insert i to ans
                return ans;
            }
            else{
                mp[nums[i]]=i;
            }
        }
        return ans;

    }
};

/* My ans */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i;
        int j;
        for(i = 0; i < nums.size(); i++) {
            int diff =  target - nums[i];
            //cout << diff ;
            for(j = 0; j < nums.size(); j++){
                if (nums[j] == diff && j!= i)
                    return {i,j};
            }
        } 
        return {};
    }
};
