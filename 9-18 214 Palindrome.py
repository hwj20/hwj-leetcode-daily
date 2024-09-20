'''
214
You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.
'''

'''
try to find the longest Palindorme from 0th
'''

def longest_palindrome_from_start_manacher(s: str) -> str:
    # Step 1: 字符串预处理
    t = '#'.join(f"^{s}$")
    n = len(t)
    P = [0] * n  # P 数组，用来记录每个字符为中心的最长回文半径
    C = R = 0  # C 是当前回文中心，R 是当前回文能扩展到的最右端
    
    for i in range(1, n - 1):
        # Step 2: 利用对称性初始化 P[i]
        if i < R:
            P[i] = min(R - i, P[2 * C - i])
        
        # Step 3: 向两边扩展，以 i 为中心
        while t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1
        
        # Step 4: 更新回文中心 C 和右边界 R
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    # Step 5: 找到 P 数组中以开头为起点的最大回文子串
    max_len_from_start = 0
    for i in range(1, n - 1):
        # 找到回文子串覆盖字符串开头的最大长度
        if i - P[i] == 1:  # 这里的1是指预处理字符串t中的第二个字符'#'的位置
            max_len_from_start = max(max_len_from_start, P[i])
    
    # Step 6: 从原字符串 s 中提取最长回文子串
    return max_len_from_start

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ans = ""
        t = longest_palindrome_from_start_manacher(s)
        # i,j = 0,len(s)-1
        # while i<j:
        #     if s[i] != s[j]:
        #         ans = ans+s[j]
        #         j -= 1
        #         i = 0
        #     else:
        #         l = i
        #         r = j
        #         is_palindrome = True
        #         while l<r:
        #             if s[l] != s[r]:
        #                 is_palindrome = False
        #                 break
        #             l += 1
        #             r -= 1
        #         if is_palindrome:
        #             break
        #         else:
        #             ans = ans+s[j]
        #             j -= 1
        #             i = 0
        print(t)
        ans += s[len(s)-1:t-1:-1]
        ans += s
        return ans
