from runner import Runner 
from utils import ListNode
from typing import *

def test_add_two_numbers():
    input = "[2,4,3]\n[5,6,4]\n[0]\n[0]\n[9,9,9,9,9,9,9]\n[9,9,9,9]"
    
    class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummyHead = ListNode(0)
            tail = dummyHead
            carry = 0

            while l1 is not None or l2 is not None or carry != 0:
                digit1 = l1.val if l1 is not None else 0
                digit2 = l2.val if l2 is not None else 0

                sum = digit1 + digit2 + carry
                digit = sum % 10
                carry = sum // 10

                newNode = ListNode(digit)
                tail.next = newNode
                tail = tail.next

                l1 = l1.next if l1 is not None else None
                l2 = l2.next if l2 is not None else None

            result = dummyHead.next
            dummyHead.next = None
            return result
    
    sol = Solution()
    question = sol.addTwoNumbers
    result = Runner(input, question).run_tests()
    golden = ["[7,0,8]", "[0]", "[8,9,9,9,0,0,0,1]"]
    
    assert result == golden, f"Test failed: {result} != {golden}"
    print("All tests passed!")