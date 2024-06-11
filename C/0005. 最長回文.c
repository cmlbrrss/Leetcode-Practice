#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* longestPalindrome(char* s) {
    
    int sLen = strlen(s);
    
    // 配置儲存空間給區域變數最大字串
    char* max_pal = (char*)malloc((sLen + 1) * sizeof(char)); 
    if (max_pal == NULL) return NULL;
    max_pal[0] = '\0';
    
    // 回文大小奇數(有中心)
    for (int center = 0; center < sLen ; center++){  
        int i = center, j = center;
        int pal_len = 0;
        while(i >= 0 && j < sLen && s[i] == s[j]){
            pal_len = j - i + 1;
            i--;
            j++;    
        }
        if (strlen(max_pal) < pal_len){
            strncpy(max_pal, s + i + 1, pal_len);
            max_pal[pal_len] = '\0';
        }
    }
    
    // 回文大小偶數(純對稱)
    for (int center = 0; center < sLen ; center++){  
        int i = center, j = center + 1;
        int pal_len = 0;
        while((i >= 0 && j < sLen) && s[i] == s[j]){
            pal_len = j - i + 1;
            i--;
            j++;
        }
        if (strlen(max_pal) < pal_len){
            strncpy(max_pal, s + i + 1, pal_len);
            max_pal[pal_len] = '\0';
        }
    }
    
    return max_pal;
}
