from runner import Runner 
from typing import *
from math import *
from functools import *

def test_regular_expression_matching():
    input = '"aa"\n"a"\n"aa"\n"a*"\n"ab"\n".*"'
    
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            
            pattern = []
            p = " " + p + " "
            prev = p[0]
            for i in range(1, len(p)):
                if p[i] == "*":
                    if len(pattern) == 0:
                        pattern.append((prev, inf))
                    elif prev == ".":
                        while len(pattern) > 0 and pattern[-1][1] == inf:
                            pattern.pop()
                        pattern.append((prev, inf))
                    else:
                        if pattern[-1] == (".", inf):
                            pass
                        elif pattern[-1] == (prev, inf):
                            pass
                        else:
                            pattern.append((prev, inf))                    
                elif prev.isalpha() or prev == ".":
                    pattern.append((prev, 1))
                prev = p[i]

            @cache
            def solve(s_idx, p_idx):
                if s_idx == len(s):
                    for q in range(p_idx, len(pattern)):
                        if pattern[q][1] == 1:
                            return False
                    return True
                elif p_idx == len(pattern):
                    return False

                if pattern[p_idx][1] == 1:
                    if pattern[p_idx][0] == s[s_idx] or pattern[p_idx][0] == ".":
                        return solve(s_idx+1, p_idx+1)
                    else:
                        return False
                else:
                    r = solve(s_idx, p_idx+1)
                    for i in range(s_idx, len(s)):
                        if pattern[p_idx][0] == "." or s[i] == pattern[p_idx][0]:
                            r |= solve(i+1, p_idx)
                        else:
                            break
                    return r
            return solve(0, 0)
    
    sol = Solution()
    question = sol.isMatch
    result = Runner(input, question).run_tests()
    golden = ["false", "true", "true"]
    
    assert result == golden, f"Test failed: {result} != {golden}"
    print("All tests passed!")
    
def test_generate_parentheses():
    input = '"2"\n"3"\n"123"\n"456"'
    
    class Solution:
        def multiply(self, num1: str, num2: str) -> str:        
            s = ''
            q = [0]*(len(num1)+len(num2))
            for i in range(len(num1)):
                for j in range(len(num2)):
                    a = int(num1[i])
                    b = int(num2[j])
                    q[i+j] += a*b

            for i in range(len(q)-2, -1, -1):
                q[i] += q[i+1] // 10
                q[i+1] = q[i+1] % 10

            for i in range(len(q)-1, -1, -1):
                q[i] = q[i-1]
            q[0] = q[1] // 10 
            q[1] %= 10

            ret = ''
            for i in q:
                ret += str(i)
            
            for i in range(len(ret)):
                if (ret[i] != '0'):
                    return ret[i:]

            return '0'

    sol = Solution()
    question = sol.multiply
    result = Runner(input, question).run_tests()
    golden = ['"6"', '"56088"']
    
    assert result == golden, f"Test failed: {result} != {golden}"
    print("All tests passed!")
    