from utils import TreeNode, ListNode
from collections import *
from bisect import *
from heapq import *
from queue import *
from math import *
from random import *
from functools import *
from string import *
from itertools import *
from re import *
from typing import *

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            num = 0
            while i < len(traversal) and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(num)
            
            while len(stack) > depth:
                stack.pop()
            
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
        
        return stack[0] if stack else None

## settings
sol = Solution()
question = sol.recoverFromPreorder