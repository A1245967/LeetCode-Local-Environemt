from typing import *
from collections import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        serialized = ""
        if self:
            queue = deque([self])
            result = []

            while queue:
                node = queue.popleft()

                if node:
                    result.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append("null")

            # remove trailing nulls
            while result and result[-1] == "null":
                result.pop()
            serialized = ",".join(result)
        return "[" + serialized + "]"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        current = self
        result = "["
        while current:
            result += str(current.val) + ","
            current = current.next
        return result[:-1] + "]"

    @classmethod
    def of(Cls, lst: List[Any]) -> Optional['ListNode']:
        head = None
        for val in reversed(lst):
            head = Cls(val, head)
        return head

    def __iter__(self):
        head = self
        while head:
            yield head.val
            head = head.next

def build_tree(leet_code_input: str) -> Optional[TreeNode]:
    """
    Credit to LeetCode user 'bqrkhn' for this function

    Given the typical leet code input string for
    a tree, where the tree is defined level by
    level such that input[i] has nodes defined
    for a level as input[i+1:nodes_in_level],
    this builds that tree!

    it returns the root of the constructed tree regardless
    """
    leet_code_input = leet_code_input[1:-1].split(',')
    if len(leet_code_input) == 0:
        return
    nodes = [('root', leet_code_input[0])]
    for index, current_node in enumerate(leet_code_input[1:]):
        if current_node != 'null':
            if index & 1:
                nodes.append((nodes[index // 2][0] + '.right', current_node))
            else:
                nodes.append((nodes[index // 2][0] + '.left', current_node))
    root = TreeNode(int(nodes[0][1]))
    for node in nodes:
        execution_statement: str = node[0] + ' = TreeNode(' + node[1] + ')'
        exec(execution_statement)
    return root
