'''
432. All O`one Data Structure
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

'''


'''
'''

class AllOne:

    def __init__(self):
        self.key_count = {}  # 哈希表：存储每个key的计数
        self.count_keys = {}  # 哈希表：存储每个计数对应的key集合
        self.min_count = 0 # 记录最小计数
        self.max_count = float('-inf')  # 记录最大计数

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            # 从当前计数集合中删除key
            self.count_keys[count].remove(key)
            if not self.count_keys[count]:
                del self.count_keys[count]
        else:
            count = 0

        # 增加key的计数
        new_count = count + 1
        self.key_count[key] = new_count

        # 把key放入新计数的集合中
        if new_count not in self.count_keys:
            self.count_keys[new_count] = set()
        self.count_keys[new_count].add(key)

        # 更新最大和最小计数
        self.max_count = max(self.max_count, new_count)
        self.min_count = min(new_count,self.min_count)
        if count == self.min_count and not self.count_keys.get(self.min_count, None):
            self.min_count = self.min_count + 1

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        # 从当前计数集合中删除key
        self.count_keys[count].remove(key)
        if not self.count_keys[count]:
            del self.count_keys[count]

        # 减少key的计数
        if count == 1:
            del self.key_count[key]
        else:
            new_count = count - 1
            self.key_count[key] = new_count
            if new_count not in self.count_keys:
                self.count_keys[new_count] = set()
            self.count_keys[new_count].add(key)

        # 更新最大和最小计数
        if count == self.max_count and not self.count_keys.get(count, None):
            self.max_count = self.max_count - 1
        if count == self.min_count and count != 1:
            self.min_count = self.min_count - 1
        if count == 1:
            c = 0
            for k in self.count_keys:
                if c == 0:
                    c = k
                else:
                    c = min(c,k)
            self.min_count = c

    def getMaxKey(self) -> str:
        if self.max_count == float('-inf') or self.max_count not in self.count_keys:
            return ""
        return next(iter(self.count_keys[self.max_count]))

    def getMinKey(self) -> str:
        # print(self.min_count)
        if self.min_count == 0 or self.min_count not in self.count_keys:
            return ""
        return next(iter(self.count_keys[self.min_count]))





# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()