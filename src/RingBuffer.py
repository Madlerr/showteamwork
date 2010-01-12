#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  RingBuffer based on deque.
"""
from collections import deque
 
class RingBuffer(deque):
    """
    Inherits deque, pops the oldest data to make room
    for the newest data when size is reached
    """
    def __init__(self, size):
        deque.__init__(self)
        self.size = size
        
    def overfull_append(self, item):
        """
          Append from right and pop leftest item
          (RingBuffer if «overfull»).
        """
        deque.append(self, item)
        # full, pop the oldest item, left most item
        self.popleft()
        
    def append(self, item):
        """
        Append item.
        If RingBuffer is full, switch to «overfull» mode.
        """
        deque.append(self, item)
        if len(self) == self.size:
            #If RingBuffer is full, switch to «overfull» mode.
            self.append = self.overfull_append
    
    def get(self):
        """
        returns a list of size items (newest items)
        """
        return list(self)
 
            