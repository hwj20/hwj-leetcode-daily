'''
1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
'''

'''
我今天要赶due，让GPT写个答案
'''



class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefixXOR = [0] * (n + 1)

        # Calculate prefix XOR
        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]

        count = 0

        # Iterate over all pairs (i, k)
        for i in range(n):
            for k in range(i + 1, n):
                if prefixXOR[k + 1] == prefixXOR[i]:
                    count += (k - i)
        # print(prefixXOR)

        return count