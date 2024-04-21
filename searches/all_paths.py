"""_summary_
Generate all possible paths from my starting point to my ending point
"""

import collections
class DeepFirstSearch:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.stack = collections.deque()
        self.stack.append([start_point])
        
    
    def search(self):
        top = self.stack.pop()
        