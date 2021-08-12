Link : https://leetcode.com/problems/valid-parentheses/

Approach  :
step 1: We just need to take empty stack .
Step 2: If we get any opening parentheses( '{','(','[' ) push it in stack.
Step 3: If we get any closing parentheses( '}',')',']' ) then check peek() of stack is having same opening or not
Step 4: If we have same opening as close then pop() if not having same opening as close true false
Step 5: At the end check if stack is empty return true or return false
