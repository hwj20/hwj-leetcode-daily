'''
564
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.
'''


'''

'''

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # res = min(ans, 999,2002)
        # flag = True
        # for i in range(int(len(n)//2)):
        #     if res[i] != res[-(i+1)]:
        #         flag = False
        # if len(n) == 1:
        #     return str(int(n)-1)
        # res1 = ''
        # for i in range(int(len(n)//2)):
        #     res1 += n[i]
        # if len(n) % 2 ==  1:
        #     res1 += n[int(len(n)//2)]
        # for i in range(int(len(n)//2)):
        #     res1 += res1[int(len(n)//2)-1-i]
        # if res1 == n:
        #     print('p')
        #     if len(n) % 2 ==  1:
        #         if int(n[len(n)//2]) == 0:
        #             res1 = str(int(n)+10**(len(n)//2))
        #         else:
        #             res1 = str(int(n)-10**(len(n)//2))
        #     else:
        #         if int(n[len(n)//2]) == 0:
        #             res1 = str(int(n)+10**(len(n)//2)+10**(len(n)//2-1))
        #         else:
        #             res1 = str(int(n)-10**(len(n)//2)-10**(len(n)//2-1))

        # res2 = '9'*(len(n)-1)
        # if res2 == '':
        #     res2 = '0'
        # res3 = str(int(n[0])+1)+'0'*(len(n)-2)
        # if n[0] == '9':
        #     res3 += '1'
        # else:
        #     res3 +=  str(int(n[0])+1)
        # ans = []
        # for res in [res1,res2,res3]:
        #     print(res)
        #     ans.append((abs(int(res)-int(n)),int(res)))
        # ans.sort()
        # print(ans)
        # return str(ans[0][1])
            # Edge case for small numbers
        if n == "0":
            return "1"
        if n == "1":
            return "0"

        # Generate the candidates
        length = len(n)
        num = int(n)
        
        # Some base edge case palindromes like 999 or 1001 for boundary cases
        candidates = [10**length + 1, 10**(length - 1) - 1]
        
        # Find the prefix (left half of the number)
        prefix = int(n[:(length + 1) // 2])
        
        # Generate palindromes by modifying the prefix
        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.append(int(candidate))
        
        # Remove n itself from the candidates
        candidates = [c for c in candidates if c != num]
        
        # Sort candidates based on absolute difference from n
        closest_palindrome = min(candidates, key=lambda x: (abs(x - num), x))
        
        return str(closest_palindrome)'''
145. Binary Tree Postorder Traversal
'''


'''
water
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(now):
            if now == None:
                return 

            dfs(now.left)
            dfs(now.right)
            ans.append(now.val)
        dfs(root)
        return ans