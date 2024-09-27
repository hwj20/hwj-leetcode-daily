'''
731
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
'''

'''

'''


class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if this new event would cause a triple booking
        for ostart, oend in self.overlaps:
            # If there is any overlap with double-booked intervals, return False
            if start < oend and end > ostart:
                return False

        # Now, check for double bookings and add them to overlaps if necessary
        for estart, eend in self.events:
            # Check if there is any overlap with the existing events
            if start < eend and end > estart:
                # Calculate the overlapping interval
                overlap_start = max(start, estart)
                overlap_end = min(end, eend)
                # Store the overlapping interval
                self.overlaps.append((overlap_start, overlap_end))

        # Add the new event to the list of booked events
        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)