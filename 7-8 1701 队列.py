'''
1701
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
'''

'''
队列
'''

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = 0
        wait = [x[0] for x in customers]
        now = wait[0]
        for idx in  range(len(customers)):
            if now < customers[idx][0]:
                now = customers[idx][0]
            cost = customers[idx][1]
            now += cost
            ans += now - wait[idx]
        return ans/len(customers)