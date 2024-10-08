'''
729
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''


'''
insert sort
'''

class Node():
    def __init__(self,l,r,n):
        self.l = l
        self.r = r
        self.next = n


class MyCalendar:

    def __init__(self):
        self.head = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start,end,None)
        # if self.head == None or self.head.l >
        now = self.head
        prev = None
        while now != None:
            # print(now.l,now.r,start,end)
            if now.r <= start:
                prev = now
                now = now.next
            elif not (end <= now.l  and start < now.l):
                return False
            else:
                break
        if not prev:
            node.next = self.head
            self.head = node
        else:
            node.next = prev.next
            prev.next = node
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)