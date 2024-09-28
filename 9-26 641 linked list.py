'''
641. Design Circular Deque
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
'''
'''
double linked list
'''
class Node:
    def __init__(self,val,nxt,prev):
        self.next = nxt
        self.prev = prev
        self.val = val

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = k
        self.k = 0

    def insertFront(self, value: int) -> bool:
        if self.k == self.size:
            return False
        if not self.head:
            now = Node(value,None,None)
            now.head = now.tail = now
            self.head = self.tail = now
        else:
            now = Node(value,self.head,self.tail)
            self.head.prev = now
            self.head = now
            self.tail.next = now
        self.k += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.size:
            return False
        if not self.head:
            now = Node(value,None,None)
            now.head = now.tail = now
            self.head = self.tail = now
        else:
            now = Node(value,self.head,self.tail)
            self.tail.next = now
            self.tail = now       
            self.head.prev = now     
        self.k += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.k == 0:
            return False
        if self.k == 1:
            self.head = self.tail = None
            self.k -= 1
            return True
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.k -= 1
        return True


    def deleteLast(self) -> bool:
        if self.k == 0:
            return False
        if self.k == 1:
            self.head = self.tail = None
            self.k -= 1
            return True
        self.tail = self.tail.prev
        self.head.prev = self.tail
        self.tail.next = self.head
        self.k -= 1
        return True        

    def getFront(self) -> int:
        if self.k == 0:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.k == 0:
            return -1
        return self.tail.val        

    def isEmpty(self) -> bool:
        return self.k == 0

    def isFull(self) -> bool:
        return self.k == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()