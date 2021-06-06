
from solution import Solution
from solution import ListNode


l1= ListNode(2,ListNode(4,ListNode(3)))   
l2= ListNode(5,ListNode(6,ListNode(4)))
o1= [7,0,8]
output = Solution().addTwoNumbers(l1,l2)
output_array = [output.val, output.next.val, output.next.next.val] 
print (output_array)
assert o1 == output_array, 'Test Case 1 Failed'
# assert [0] == Solution().addTwoNumbers([0], [0]) , 'Test Case 2 Failed'
# assert [1,4,5] == Solution().addTwoNumbers([0,3,4], [1,2,1]) , 'Test Case 3 Failed'
print ("successfully done")
