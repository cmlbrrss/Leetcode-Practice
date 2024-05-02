using namespace std;
class Solution {
public:
    string longestPalindrome(string s) {
        string max_pal = "";
        string pal;
        int n = 0;
        while(n < s.size()){
            int i = n, j = n;
            while ((i >= 0 && j < s.size()) && s[i] == s[j]){
                pal = s.substr(i,j-i+1);
                i--;
                j++;
            }
            if (pal.size() > max_pal.size()) {
                max_pal = pal;
                }  
            n++;
        }   
        n = 0;
        while(n < s.size()){
            int i = n;
            int j = n + 1;
            while ((i >= 0 && j < s.size()) && s[i] == s[j]){
                pal = s.substr(i,j-i+1);
                i--;
                j++;
            }
            if (pal.size() > max_pal.size()) {
                max_pal = pal;
                }     
            n++; 
        }
        return max_pal;
    }
};
