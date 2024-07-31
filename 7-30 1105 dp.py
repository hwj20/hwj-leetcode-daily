'''
1105. Filling Bookcase Shelves
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
'''

'''
不解,dfs 会t掉
dp[i][res] = min(
    
    
    dp[i-1][>res+thick[i]](h>=height)],dp[i-1][>res+thick[i]+height_cost))
    debug了半天，我发现我的方法就是错的

'''



class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # global ans
        # ans = float('inf')

        # def dfs(now,res,h,val):
        #     global ans
        #     # print(now,res,h,val)
        #     if val >= ans:
        #         return
        #     if now == len(books):
        #         ans = min(ans,val)
        #         return
        #     # print(books[now])
        #     if books[now][1] <= h and books[now][0]<=res:
        #         dfs(now+1,res-books[now][0],h,val)
        #         return 
        #     if  books[now][0] > res :
        #         dfs(now+1,shelfWidth-books[now][0],books[now][1],val+books[now][1])
        #         return
        #     dfs(now+1,res-books[now][0],books[now][1],val-h+books[now][1])
        #     dfs(now+1,shelfWidth-books[now][0],books[now][1],val+books[now][1]) # new line
        # dfs(1,shelfWidth-books[0][0],books[0][1],books[0][1])
        # return ans
        # n = len(books)
        # dp = [[(float('inf'),-1)]*(shelfWidth+1) for _ in range(n)]
        # lm = [float('inf')]*n
        # for i in range(shelfWidth-books[0][0]+1):
        #     dp[0][i] = (books[0][1],books[0][1])
        # lm[0] = min(lm[0],books[0][1])

        # for i in range(1,n):
        #     for j in range(shelfWidth+1):
        #         idx = j + books[i][0]
        #         # print(idx,dp[i-1][idx])
        #         if j <= shelfWidth - books[i][0]:
        #             dp[i][j] = (min(dp[i][j][0],lm[i-1]+books[i][1]),books[i][1])
        #         if  idx<= shelfWidth and dp[i-1][idx][0] != float('inf'):

        #             if dp[i-1][idx][1] >= books[i][1]:
        #                 if dp[i-1][idx][0] <= dp[i][j][0]:
        #                     dp[i][j] = (dp[i-1][idx][0],dp[i-1][idx][1])
        #             else:
        #                 cost  = books[i][1]-dp[i-1][idx][1]
        #             # print(cost)
        #                 if dp[i-1][idx][0]+cost <= dp[i][j][0]:
        #                     dp[i][j] = (dp[i-1][idx][0]+cost,books[i][1])
        #         lm[i] = min(lm[i],dp[i][j][0])
        # print(dp[n-4][:30],dp[n-3][:30])
        # return lm[n-1]

        n = len(books)

        f = [0] * (n + 1)

        for i, (w, h) in enumerate(books, 1):

            f[i] = f[i - 1] + h

            for j in range(i - 1, 0, -1):

                w += books[j - 1][0]

                if w > shelfWidth:

                    break

                h = max(h, books[j - 1][1])

                f[i] = min(f[i], f[j - 1] + h)

        return f[n]    
