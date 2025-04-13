from runner import Runner 
from typing import *

def test_two_sum():
    input = "[2,7,11,15]\n9\n[3,2,4]\n6\n[3,3]\n6"
    
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            dict = {}
            for i in range(len(nums)):
                dict[target -nums[i]] = i
                
            for i in range(len(nums)):
                ans = dict.get(nums[i], None)
                if ans != None and ans != i:
                    return [i, ans]
    
    sol = Solution()
    question = sol.twoSum
    result = Runner(input, question).run_tests()
    golden = ["[0,1]", "[1,2]", "[0,1]"]
    
    assert result == golden, f"Test failed: {result} != {golden}"
    print("All tests passed!")