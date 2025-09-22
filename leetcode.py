from typing import List


# nums=[2,2,2,2,23,41,3,4,1,4,12,2,3]
# # k=2
# # def Remover(nums,k):
# #     l=len(nums)
    
# #     for i in nums:
# #         if i==k:
# #             nums.remove(i)
# #     print(nums)
# #     return len(nums)





# # Remover(nums,k)

# def removeDuplicates(nums):
#     unique=set(nums)
#     c=[]

#     for i in unique:
#         c.append(i)
    
#     c.sort()
    
#     return c

    
#     # for i in nums:
#     #     if i in nums:
#     #         nums.remove(i)

#     #     print(i)
#     # print(nums)
    
#     # return len(nums)


# removeDuplicates(nums)




# nums=[-1,1]


# def order():
#     data=[]
#     neg=[]
#     final=[]
#     for i in nums:
#         if i <= 0:
#             neg.append(i)
#         if i >= 0:
#             data.append(i)

#     for i,j in zip(data,neg):
#         final.append(i)
#         final.append(j)
            
            
#     print(final)
        
# order()     
        
        
# def power(x):
#     for i in range(31):
#         if 2**i==x:
            
#             print(True)
#             return True
            
#             break
            
#         else:
            
#             print(False)
#     return False

# power(16)


# nums=[0,1,2,4,5,6,7,8]
# def missingNumber(nums):
#     nums.sort()
    
#     c=len(nums)
#     d=[]
#     for i in range(c+1):
#         d.append(i)
        
#     a=set(d)
#     b=set(nums)
#     f=list(a-b)
        
    
#     print(g)
    
    
# missingNumber(nums)


# ERHtw5j7GAH4Kg2MjGnKQO7E\
    
    
    
# board =[["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]



# def isValidSudoku(board):
#     check=set()
#     for j in range(10):
#         for i in board[j]:
#             if i in check:
#                 print(i)
#                 print(check)
                
#                 return False
#             check.add(i)
    

# isValidSudoku(board)


# if isValidSudoku(board):
#     print("Duplicate found!")
# else:
#     print("No duplicates.")


# num1=[3,4,5,2]
# num2=[1,5,6,4,2]


# def sort(num1,num2):
#     num1.sort()
#     for i in range(len(num1)):
#         if num1[i] in num2:
#             return num1[i]
    
#     return -1

# sort(num1,num2)
 
 
 
    
# intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval=[4,8]
    
# def insert(intervals, newInterval):
#     for i in range(len(intervals)):
#         a=intervals[i]
#         print(a[0])
#         if newInterval[0] 
#             # if a[1]<=newInterval[1]:
#             #     print(a[0],a[1])
            
   

# def insert(intervals, newInterval):
#     n=len(intervals)
#     reslut=[]
#     i=0
    
#     while i < n and intervals[i][1]<newInterval[0]:
#         reslut.append(intervals[i])
#         i+=1
        
#     while i < n and intervals[i][0]<=newInterval[1]:
#         newInterval[0]=min(newInterval[0],intervals[i][0]) 
#         newInterval[1]=max(newInterval[1],intervals[i][1])
#         i+=1
#     reslut.append(newInterval)
    
#     while i<n :
#         reslut.append(intervals[i])
#         i+=1
        
#     return reslut

# insert(intervals,newInterval)



 
# def findMinArrowShots(points):
#     if not points:
#         return 0
    
#     # Sort the balloons based on their end points
#     points.sort(key=lambda x: x[1])
    
#     arrows = 1
#     end = points[0][1]  # End point of the first balloon
    
#     for start, end_balloon in points[1:]:
#         # If the start point of the current balloon is beyond the end point of the arrow,
#         # a new arrow is needed, so increment the count and update the end point
#         if start > end:
#             arrows += 1
#             end = end_balloon
    
#     return arrows

# # Example usage:
# points = [[10,16],[2,8],[1,6],[7,12]]



# print(findMinArrowShots(points))  # Output should be 2

 
 
 
 
# findMinArrowShots(points)


# def count_subarrays(nums, k):
#     def count_subarrays_with_max_at_least_k(max_val):
#         count = 0
#         curr_count = 0
#         left = 0
#         for right in range(len(nums)):
#             if nums[right] <= max_val:
#                 curr_count += 1
#                 if curr_count == k:
#                     while nums[left] > max_val:
#                         left += 1
#                     count += len(nums) - right
#                     left += 1
#                     curr_count -= 1
#             else:
#                 left = right + 1
#                 curr_count = 0
#         return count

#     return count_subarrays_with_max_at_least_k(max(nums)) - count_subarrays_with_max_at_least_k(max(nums) - 1)

# # Example usage:
# nums = [1, 2, 1, 2, 6]
# k = 2
# print(count_subarrays(nums, k))  # Output: 7


# def count_subarrays(v, k):
#     m = {}
#     n = len(v)
#     a = max(v)
#     i = j = 0
#     ans = 0
#     while j < n:
#         m[v[j]] = m.get(v[j], 0) + 1
#         while m.get(a, 0) >= k:
#             ans += n - j
#             m[v[i]] -= 1
#             i += 1
#         j += 1
#     return ans

# # Example usage
# nums = [1, 3, 2, 3, 3]
# k = 2
# result = count_subarrays(nums, k)
# print(f"Number of valid subarrays: {result}")


# def count_subarrays(nums, k):
#     n=nums
#     a=max(n)
#     count=0
    
#     for i in nums:


#         while nums[i-1]==a and k!=0:
#             k=k-1
#             nums.pop()
#             print(k,n)
#             i+1
#             count+1

#     print("count",count)


# # Example usage
# nums = [1, 3, 2, 3, 3]
# k = 2
# result = count_subarrays(nums, k)
# print(f"Number of valid subarrays: {result}")


# def lengthOfLastWord(s):
#     a=""
#     for element in range(0, len(s)):
#         print(s[element])
    
        
# s = "Hello World"
# lengthOfLastWord(s)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
        
# def removeZeroSumSublists(head):
#     dummy = ListNode(0)
#     dummy.next = head
#     prefix_sum = 0
#     prefix_sum_dict = {}
#     current = dummy
    
#     print(dummy)

        
            
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(-3)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(1)

# # Remove consecutive sequences that sum to zero
# result = removeZeroSumSublists(head)

# removeZeroSumSublists(head)

# def isomorpic(s,t):
#     s_to_t={}
#     t_to_s={}
    
#     if len(s)==len(t):
#         for i in range(len(s)):
#             if s[i] in s_to_t:
#                 print("nope")
    


# s="egg"
# t="add"
# isomorpic(s,t)
    
# def lengthOfLastWord(s):
#     words = s.split()

    
    
#     if not words:
#         print(words)
        
#         return 0
#     print(words)
#     return len(words[-1])

# s="egg is the best"

# lengthOfLastWord(s)

# board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word="SEED"

# def exist(board, word):
#     def backtrack(row,col,idx):
#         if idx==len(word):
#             print(idx)
#             return True
        
#         if row<0 or row>=len(board) or col<0 or col >=len(board[0]) or board[row][col] != word[idx]:
#             return False
#         temp= board[row][col]
#         board[row][col] = '#'
        
#         found=(backtrack(row+1,col,idx+1)or 
#                backtrack(row-1,col,idx+1)or
#                backtrack(row,col+1,idx+1)or
#                backtrack(row,col-1,idx+1))
#         board[row][col]=temp
#         return found
        
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j]== word[0] and backtrack(i,j,0):
#                 return True
            
#     return False
        
        
        
# exist(board, word)


# def exist(board, word):
#     def backtrack(row, col, idx):
#         if idx == len(word):
#             return True
        
#         if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[idx]:
#             return False
        
#         temp = board[row][col]
#         board[row][col] = '#'
        
#         found = (backtrack(row + 1, col, idx + 1) or
#                  backtrack(row - 1, col, idx + 1) or
#                  backtrack(row, col + 1, idx + 1) or
#                  backtrack(row, col - 1, idx + 1))
        
#         board[row][col] = temp
        
#         return found
    
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == word[0] and backtrack(i, j, 0):
#                 return True
    
#     return False

# # Example usage:
# board = [
#     ['A','B','C','E'],
#     ['S','F','C','S'],
#     ['A','D','E','E']
# ]
# word = "SEE"
# print(exist(board, word))  # Output: True
# s="((*)))"
# def checkValidString(s):
#     open_brackets=closed_brackets=0
    
#     for char in s:
#         if char == '(':
#             open_brackets += 1
#             closed_brackets += 1
#         elif char == ')':
#             open_brackets = max(0, open_brackets - 1)
#             closed_brackets -= 1
#         elif char == '*':
#             open_brackets = max(0, open_brackets - 1)
#             closed_brackets += 1
        
#         if closed_brackets < 0:
#             return False

#     return closed_brackets == 0
        
        
    
# checkValidString(s)

# tickets = [2,3,5,1]
# k = 2

# def BuyTicket(ticket,k):
#     time=0
    
#     for i in range(len(ticket)):

#         if ticket[i]>=0:
#             ticket[i]=ticket[i]-1
#             time+=1
            
#             if i==k and ticket[i]==0:
#                 return time
#     if ticket[k] == 0:
#         return -1
            
    
# BuyTicket(tickets,k)



# def time_to_buy_ticket(tickets, k):
#     n = len(tickets)
#     remainingTickets = tickets.copy()
#     time = 0

#     while True:
#         for i in range(n):
#             if remainingTickets[i] > 0:
#                 remainingTickets[i] -= 1
#                 time += 1
#                 if i == k and remainingTickets[i] == 0:
#                     return time
                
#         # Check if the k-th person has left the line
#         if remainingTickets[k] == 0:
#             return time

# tickets = [2, 3, 4, 5]
# k = 1
# print(time_to_buy_ticket(tickets, k))  # Output: 4


# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         time=0
#         ticket=tickets.copy()
#         n = len(tickets)
#         while True:    
#             for i in range(n):

#                 if ticket[i]>=0:
#                     ticket[i]-=1
#                     time+=1

#                     if i==k and ticket[i]==0:
#                         return time
#             if ticket[k] == 0:
#                 return time



# years=2000

# def is_leap(year):
#     leap = False
#     if year%4==0 and year%100!=0:
#         leap=True
        
#     elif year%100==0 and year%400==0:
#             leap=True
            
#     else:
#             leap=False
            
    
#     return leap

# print(is_leap(years))

# num=1234
# k=2

# def removek(num,k):
#     k=0
    
# removek(num,k)


# class Solution:
#     def numSteps(self, s):
#         a=int(s,2)
#         i=0
        
#         while a!=1:
#             if a%2==0:
#                 a//=2
#                 print(a)
#                 i+=1
#             else:
#                 a=a+1
#                 i+=1
#         return i
        
        
# obj1=Solution()
# obj1.numSteps("1111011110000011100000110001011011110010111001010111110001")

# a="hello"


# def asc(a):
#     b=0
#     values=[]
#     arrsum=[]
#     for i in range(len(a)):
#         values.append(ord(a[i]))
    
#     for j in range(len(values)-1):
#         d=values[j]-values[j+1]
#         if d<0:
#             d=d*-1
#             arrsum.append(d)
#         else:
#             arrsum.append(d)
        
#     for k in range(len(arrsum)):
#         z=sum(arrsum)
        
#     return z
    

# asc(a)

# from typing import List, Optional 

# # nums = [1,3,5,6]
# # target = 7

# # class Solution:
# #     def searchInsert(self, nums: List[int], target: int) -> int:
# #         for i,j in enumerate(nums):
# #             if(j==target):
# #                 return i
                
# #             elif target<nums[0]:
# #                 return 0
# #             elif target>nums[-1]:
# #                 return len(nums)-1

# #             elif (nums[i]<target and nums[i+1]>target):
# #                 return i+1

# # obj=Solution()

# # obj.searchInsert(nums,target)


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         list3=ListNode(0)
#         current=list3

#         while list1 and list2:

#             if list1.val <= list2.val:
#                 current.next=list1
#                 list1=list1.next
#             else:
#                 current.next=list2
#                 list2=list2.next
#             current=current.next

#             if list1:
#                 current.next=list1
#             if list2:
#                 current.next=list2
            

#         return list3.next
#             # if list1.val<list2.val:
#             #     list3.append(list1.val)
#             #     continue
#             # else:
#             #     list3.append(list2.val)
#             #     continue

            

#         # print(list3)




# prices = [7,1,5,3,6,4]
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#       l,r=0,1
#       max_profit=0


#       while(r<len(prices)):
#         if prices[l]<prices[r]:
#           max_profit=max(max_profit,prices[r]-prices[l])
#           print(max_profit)

#         else:
#           l=r
#         r+=1

      
#       if max_profit:
#         print(max_profit)
#         return max_profit
#       else:
#         print(0)
#         return 0
        

# item=Solution()
# item.maxProfit(prices)

# prices=[7,1,5,3,6,4,54,4,8,9]
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit=0
#         for i in range(1,len(prices)):
#           if prices[i]>prices[i-1]:
#             profit+=prices[i]-prices[i-1]

#         print(profit)
#         return profit
   
# nums = [6,5,5]
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#       set_val=set(nums)
#       new=list(set_val)
#       print("new=",new)
#       max_val=0
#       for i in range(len(new)):
#         print(max_val,i,new[i],"current max",nums.count(new[i]))

#         if nums.count(new[i])>=max_val:

#           # print(nums.count(new[i]))
#           max_val=nums.count(nums[i])
#           number=new[i]
        
        
#       print(max_val)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#       n=len(nums)/2
#       set_val=set(nums)
#       new_li=list(set_val)
#       for i in range(len(new_li)):
#         if nums.count(new_li[i])>=n:
#           print(new_li[i])


# obj=Solution()
# obj.majorityElement(nums)

# s = "1011011"

# class Solution:
#     def maxScore(self, s: str) -> int:
#         string=list(s)
#         one=list(string)
#         one.reverse()
#         one_count=0
#         two_count=0
#         score=0
#         two=[]
#         two.append(string[0])
#         one.pop()

#         for i in range(1,len(string)):
#           two_count=two.count("0")
#           one_count=one.count("1")

#           if score<=two_count+one_count:
#             score=two_count+one_count

#           if len(one)>1:
#             two.append(string[i])
#             one.pop()

#         print(score)
#         return score



# obj=Solution()
# obj.maxScore(s)


# s = "abc"
# shifts = [[4,3],[1,1],[0,2]]

# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
#         call_back={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

#         for i in s:
#             print(call_back)

        


# obj=Solution()
# obj.shiftingLetters(s,shifts)

# strs = ["flower","flow","flight"]
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         l,r=0,0
#         run=list[strs]

#         long=strs[0]

#         for i in range(len(strs)):
#             for j in range(len(strs[i])):
#                 for k in range(len(long)):
#                     if long[i][j]==strs[i][j]:
#                         print(strs[i][j])
       
        
#         # while(r<len(strs)):
#         #     if strs[l][r]==strs[l+1][r]:
#         #         print(strs[l][r])
#         #     r+=1
#         # l+=1

# obj=Solution()
# obj.longestCommonPrefix(strs)

# boxes = [1,3,2,2,2,3,4,3,1]
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         pass


# obj=Solution()
# obj.minOperations(boxes)

# words = ["leetcoder","leetcode","od","hamlet","am"]
# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:

#         new=[]

#         for i in range(len(words)):
#             check=words[i]
#             for j in range(len(words)):
             
                
#                 if check!=words[j]:
#                     if check in words[j] and check not in new: 
                        
#                         new.append(check)
        
#         print(new)
# obj=Solution()
# obj.stringMatching(words)


# words=["pa","papa","ma","mama"]

# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         print(words)
#         for i in range(len(words)):
#             for j in range(i,len(words)):
#                 print(words[i])


#                 '''1.take the first word and check it with the second one
#                    2.slice the second word word[j].slice(:len(word[i]))  and  word[j],slice[len(word):-1] '''


# obj=Solution()
# obj.countPrefixSuffixPairs(words)


# words1=["amazon","apple","facebook","google","leetcode"]

# words2=["e","o"]
# class Solution:
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         pass


# obj=Solution()
# obj.wordSubsets(words1,words2)


# s="ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"
# class Solution:
#     def minimumLength(self, s: str) -> int:
#         set_of_letter=set(s)
#         list_of_letter=list(set_of_letter)

#         total=[]
#         # print(list_of_letter)

#         for i in range(len(list_of_letter)):
#             current_char_count=s.count(list_of_letter[i])
#             letter=s[i]
#             # print(current_char_count)
#             a=0
#             if current_char_count>2:
#                 # print(current_char_count)
            
#                 while (current_char_count>2):
#                     a=current_char_count-2
#                     current_char_count=-2
#                 total.append(a)
#             else:
#                 total.append(current_char_count)

#             # print(a)
            
#         print(sum(total))
#         return sum(total)


#     '''1.get a char with minimum leg greater than 2.
#     2.if s[i].count>2 then we need to take out the first value and skip the second and then take out third.
#     3.'''


# obj=Solution()
# obj.minimumLength(s)

# A=[1,2,3,4,5]
# B=[2,4,6,8,10]
# class Solution:
#     def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
#         pass
#         '''1.get a char with minimum leg greater than 2.
#     2.if s[i].count>2 then we need to take out the first value and skip the second and then take out third.
#     3.'''

# obj=Solution()
# obj.findThePrefixCommonArray(A,B)

# grid=[[1,2,3],[4,5,6],[7,8,9]]
# class Solution:
#     def minCost(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         cost = [[float('inf')] * n for _ in range(m)] 
#         cost[0][0] = grid[0][0]  

#         heap = [(grid[0][0], 0, 0)]

# obj=Solution()
# obj.minCost(grid)


# s="daabcbaabcbc"
# part="abc"
# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         while part in s:
#             s = s.replace(part, "", 1)  
#         return s

# obj=Solution()
# obj.removeOccurrences(s,part)


# s="abc"
# class Solution:
#     def clearDigits(self, s: str) -> str:
#         pass

# obj=Solution()
# obj.clearDigits(s)


# class Solution:
#     def clearStars(self, s: str) -> str:
#         new_list=[]
#         convert=""
      

#         for loop_data in s:
#             if loop_data !="*":
#                 new_list.append(loop_data)
#             else:
              
     
#                 new_list.reverse()
#                 new_list.remove(min(new_list))
#                 new_list.reverse()    

            

        

#         joined=convert.join(new_list)
#         print(joined)
#         return joined
        



# obj=Solution()
# obj.clearStars(val)

# print(chr(11))



# class Solution:
#     def maxAdjacentDistance(self, nums: List[int]) -> int:
#         fl_diff=len(nums)-1
#         curr=0
#         now=0
#         max_di=max(nums[0]-nums[fl_diff],nums[fl_diff]-nums[0])
        
#         for i in range(len(nums)-1):
#             now=(max(nums[i]-nums[i+1],nums[i+1]-nums[i]))
#             curr=max(curr,now)
        
#         return max(curr,max_di)
                
                

# obj=Solution()
# nums=[-1,-9,-8]
# obj.maxAdjacentDistance(nums)


# num=99999

# class Solution:
#     def minMaxDifference(self, num: int) -> int:
#         str_num=str(num)
#         max_val=0
#         min_val=0

#         for ch in str_num:
#             if ch!="9":
#                 max_val=ch
#                 break

#         max_val=str(max_val)
#         max_val=int(str_num.replace(max_val,"9"))
        
#         for ch in str_num:
#             if ch!="0":
#                 min_val=ch
#                 break

#         min_val=str(min_val)
#         min_val=int(str_num.replace(min_val,"0"))
#         return max_val-min_val

            

# obj=Solution()
# obj.minMaxDifference(num)



#sigle linked list
'''
Struct Node:
    int data;
    Node* next;

Node* Head
    
void createnewNode(int data){
    newNode=struct Node(malloc sizeof(struct Node));
    newNode->data=data;
    newNode->next=NULL;
}
    
void main(){
    
    }

void insertNode(int data){
    
    newNode=struct Node(malloc sizeof(struct Node));
    newNode->data=data;
    newNode->next=Head;
    Head=newNode;
}

'''

'''
void main(){

int n=0;
int matrix[n][n];


for (i=0;i<n;i++){
    for (j=0;j<n;j++){
        scan('%d',&matrix[i][j]);
    }
}

}




linear search

int arr[10]=[2,3,5,2,5,2,4,2,9];
n=9;
for (i=0;i<=n:i++):
    if (i==n){
        return n
    }
    else{
    return "not found"}



'''

# nums=[4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
# k=1
# class Solution:
#     def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
#         nums.sort()
#         new_list=[]
#         mid_list=[]
#         i=0

#         while(i<len(nums)):
#             mid_list.append(nums[i])
#             mid_list.append(nums[i+1])
#             mid_list.append(nums[i+2])
            

#             i+=3
#             new_list.append(mid_list)
#             mid_list=[]
            
#         for i in range(len(new_list)):

#             if max(new_list[i])-min(new_list[i])>k:
#                 return []
        
#         return new_list
        
# obj=Solution()
# obj.divideArray(nums,k)

# s = "abcdefghij"
# k = 3
# fill = "x"

# class Solution:
#     def divideString(self, s: str, k: int, fill: str) -> List[str]:
#         s= [i for i in s]
#         new=[]
#         temp=[]
#         for i in range(len(s)):
#             while (len(temp)<=k -1):
#                 temp.append(s[i])
#                 temp.append(s[i])
        
#         print(temp)


# obj1=Solution()
# obj1.divideString(s,k,fill)


# class Solution:
#     def possibleStringCount(self, word: str) :
#         pointer=word[0]
#         p_count=0
        
#         for i in word:
#             if pointer==i:
#                 p_count+=1
#             else:
#                 pointer=i
#         print(p_count)
                
            

# obj=Solution()
# word = "aaaa"
# obj.possibleStringCount(word)

# class Solution:
#     def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]):
#         players.sort()
#         trainers.sort()
#         print(players)
#         print(trainers)
#         count_val={}
        
#         count_main=[]
        
#         for i in range(len(players)):
#             for j in range(len(trainers)):
#                 if players[i]<=trainers[j]:
#                     count_val[trainers[j]]=players[i]
                    
                    
#                     if count_val[trainers[j]]:
#                         print("true")
#                     # else:
#                     pass
#                     #     count_val[trainers[j]]=players[i]
                    

        
#         data=len(count_val)
#         print(count_val)
#         print(count_main)
                     

# obj=Solution()
# players = [4,4] #4,7,9
# trainers = [2,4,2,2,3,2,4,2,2,3,2,2,1,1,3,3,1,3,2,3,1,3,3,4,1,2,1,2,3,2,3,4,2,2,3,1,3,4,3,3,4,3,2,2,2,1,4,2,4,4,3,1,1,4,2,1,1,4,2,2,3,4,1,1,1,4,4,1,1,4,4,4,2,3,1,1,3,2,1,2,1,1,3,4,4,2,1,4,2,3,1,3,3,4,1,4,1,4,4,1] # 2,5,8,8

# obj.matchPlayersAndTrainers(players,trainers)


# class Solution:
#     def maximumUniqueSubarray(self, nums: List[int]):
#         seen=set()
#         curr_sum=0
#         max_sum=0
#         start=0
#         max_score=0
        
#         for end in range(len(nums)):
#             while nums[end] in seen:
#                 print("end=",seen)
#                 # print("start=",nums[end])
                
#                 seen.remove(nums[start])
#                 curr_sum-=nums[start]
#                 start+=1
#             seen.add(nums[end])
#             curr_sum+=nums[end]
#             max_score=max(max_sum,curr_sum)
        
#         print(max_score)
    
# obj=Solution()
# nums=[5,2,1,2,5,2,1,2,5]
# obj.maximumUniqueSubarray(nums)

# class Solution:
#     def countHillValley(self, nums: List[int]):
#         count = 0
#         for i in range(1, len(nums) - 1):
#             if nums[i] == nums[i - 1]:
#                 continue
            
#             left = i - 1
#             while left >= 0 and nums[left] == nums[i]:
#                 left -= 1
#             right = i + 1
#             while right < len(nums) and nums[right] == nums[i]:
#                 right += 1
            
#             if left < 0 or right >= len(nums):
#                 continue
            
            
#             if nums[left] < nums[i] > nums[right]:
#                 count += 1  
#             elif nums[left] > nums[i] < nums[right]:
#                 count += 1  
#         print(count)
#         return count

    

# obj1=Solution()
# num=[6,6,5,5,4,1]
# # num=[2,4,1,1,6,5]
# obj1.countHillValley(num)

# class Solution:
#     def maximumGain(self, s: str, x: int, y: int):
#         total=0
        
        
        
#         new_list=list(s)
#         i=0
#         # for i in range(len(new_list)):
#         #     print(new_list[i])
#         #     if new_list[i]=="a":
#         #         if new_list[i+1]=="b":
#         #             print("yes")
#         #             total+=x
#         print(new_list)
#         while(i<len(new_list)-1):
            
            
#             if new_list[i]=="a":
#                 if new_list[i+1]=="b":
#                     total+=x
#                     print(new_list)
#                     new_list.remove(new_list[i])
#                     new_list.remove(new_list[i+1])
                    
#                     i=0
                    
#                     print(new_list)
#                     break
#                     continue
#             if new_list[i]=="b":
#                 if new_list[i+1]=="a":
#                     total+=y
#                     del new_list[i]
#                     del new_list[i+1]
#                     i=0
#                     # print(new_list,new_list[i],total)
                    
#                     continue
#             i+=1
            
#         print(total)
            
            
    
# obj=Solution()
# s = "cdbcbbaaabab"
# x = 4
# y = 5
# obj.maximumGain(s,x,y)

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         for i in range(numRows):
#             pass
    

# obj=Solution()
# numRows=5
# obj.generate(numRows)

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         out=[]
        
    

# obj=Solution()
# nums=[1,1,2]
# obj.permuteUnique(nums)

# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         ROWS,COLUMS=len(matrix),len(matrix[0])
#         cache={}
        
#         def helper(r,c):
#             if r>=ROWS or c>=COLUMS:
#                 return 0
            
#             if (r,c) not in cache:
#                 down=helper(r+1,c)
#                 right=helper(r,c+1)
#                 diag=helper(r+1,c+1)

#                 cache[(r,c)]=0
                
#                 if matrix[r][c]=="1":
#                     cache[(r,c)]=min(down,right,diag)+1
                    

#             return cache[(r,c)]
#         helper(0,0)
#         print(max(cache.values())**2)
#         return max(cache.values())**2
        



# obj=Solution()
# matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# obj.maximalSquare(matrix)

# matrix=[[1,1,1,1,2],[3,254,23,46,2],[32,3,5]]

# result=[x for i in matrix for x in i]
# print(result)


# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         pass
#         ROW,COLS=len(matrix),len(matrix[0])
#         cache={}
        
#         def helper(r,c):
#             if r>=ROW or c>=COLS:
#                 return 0
            
#             if (r,c) not in cache:
#                 down=helper(r+1,c)
#                 right=helper(r,c+1)
#                 diag=helper(r+1,c+1)
                
#                 cache[(r,c)]=0
                
#                 if matrix[r][c]==1:
#                     cache[(r,c)]=min(down,right,diag)+1
                    
#             return cache[(r,c)]

#         helper(0,0)
#         new=0
#         for i in cache.values():
#             if i>=1:
#                 new+=1
        
#         print(sum(cache.values()))            
        
        
        
    
# obj=Solution()
# matrix=[
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# obj.countSquares(matrix)


# cache={(1,1):1,(4,5):2,(3,4):3,(2,3):4,(5,6):1,}
# a=[x for x in cache.keys()]
# b=[]
# c=[]

# for i in range(len(a)):
#     num=a[i]
#     b.append(a[i][0])
#     c.append(a[i][1])
 
        
# print(a,b,c)

# class Solution:
#     def minimumArea(self, grid: List[List[int]]) -> int:
#         ROW,COLS=len(grid),len(grid[0])
#         cache={}
        
#         for i in range(ROW):
#             for j in range(COLS):
#                 if grid[i][j]==1:
#                     # min_row=i
#                     # max_row=i
#                     cache[i+1,j+1]=1
                    
#         a=[x for x in cache.keys()]
#         b=[]
#         c=[]

#         for i in range(len(a)):
#             num=a[i]
#             b.append(a[i][0])
#             c.append(a[i][1])
        
#         b=set(b)
#         c=set(c)
#         print(a)
        
#         if len(b)==1:
#             b=1
#         else:
#             b=max(b)
            
#         if len(c)==1:
#             c=1
#         else:
#             c=max(c)
        
#         # print(c)
#         # print(b,c)
#         d=b*c
        
#         print(d)
#         return d
        
#         # d=max(a)
#         # e=min(a)
#         # d=d[0]*d[1]
#         # if len(a)==1:
#         #     # print(1)
#         #     return 1
        
   
#         # b=set(b)
#         # c=set(c)
        
#         # if len(b)==1:
#         #     min_b=1
#         # else:
#         #     min_b=min(b)
#         #     print(min_b)
        
#         # if len(c)==1:
#         #     max_c=1
#         # else:
#         #     max_c=max(c)
#         #     print(max_c)

#         # print(min(d),min(e))
        
#         # print(min_b,max_c)
#         # return b*c
        
        
# obj=Solution()
# # grid =[[0,0,0],[0,0,0],[0,0,0],[1,0,1]]
# grid=[[0,0,0],[0,0,0],[0,0,1],[0,1,0]]
# # grid= [[0,1,0],[1,0,1]]
# obj.minimumArea(grid)

# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         ROW,COLS=0,0
#         result=[]
#         r,c=0,0
#         edge=0
#         def down(r,c):
#             if c<=len(mat[0]):
#                 result.append(mat[r][c+1])
#                 c+=1
     
#                 if r<=len(mat) and c<=len(mat[0]):
                    
#                     if c>-1:
#                         result.append(mat[r+1][c-1])
#                     elif r<len(mat):
#                         result.append(mat[r+1][c])
#                         r+=1
                        
            
                    
                        

        
#         if r==0 and c==0:
#             result.append(mat[r][c])
#             down(r,c+1)
            

#         print(result)
                
    
# obj=Solution()
# mat=[[1,2,3],[4,5,6],[7,8,9]]
# obj.findDiagonalOrder(mat)

# import math
# class Solution:
#     def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
#         final_diag = 0
#         final_area = 0

#         for l, w in dimensions:
#             diag = math.sqrt(l * l + w * w)
#             area = l * w

#             if diag > final_diag:
#                 final_diag = diag
#                 final_area = area
#             elif diag == final_diag:
#                 final_area = max(final_area, area)
        
#         print(final_area)

#         return final_area

# obj=Solution()
# dimensions=[[4,7],[8,9],[5,3],[6,10],[2,9],[3,10],[2,2],[5,8],[5,10],[5,6],[8,9],[10,7],[8,9],[3,7],[2,6],[5,1],[7,4],[1,10],[1,7],[6,9],[3,3],[4,6],[8,2],[10,6],[7,9],[9,2],[1,2],[3,8],[10,2],[4,1],[9,7],[10,3],[6,9],[9,8],[7,7],[5,7],[5,4],[6,5],[1,8],[2,3],[7,10],[3,9],[5,7],[2,4],[5,6],[9,5],[8,8],[8,10],[6,8],[5,1],[10,8],[7,4],[2,1],[2,7],[10,3],[2,5],[7,6],[10,5],[10,9],[5,7],[10,6],[4,3],[10,4],[1,5],[8,9],[3,1],[2,5],[9,10],[6,6],[5,10],[10,2],[6,10],[1,1],[8,6],[1,7],[6,3],[9,3],[1,4],[1,1],[10,4],[7,9],[4,5],[2,8],[7,9],[7,3],[4,9],[2,8],[4,6],[9,1],[8,4],[2,4],[7,8],[3,5],[7,6],[8,6],[4,7],[25,60],[39,52],[16,63],[33,56]]
# obj.areaOfMaxDiagonal(dimensions)


# from functools import lru_cache

# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
#         ROW, COLS = len(grid), len(grid[0])

#         # 4 diagonal directions (↘, ↙, ↖, ↗) in clockwise order
#         dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

#         def expected(step: int) -> int:
#             if step == 0:
#                 return 1
#             return 2 if step % 2 == 1 else 0

#         @lru_cache(None)
#         def dfs(r: int, c: int, step: int, d: int, turn_allowed: int) -> int:
#             # bounds check
#             if not (0 <= r < ROW and 0 <= c < COLS):
#                 return 0

#             # value must match expected sequence
#             if grid[r][c] != expected(step):
#                 return 0

#             best = 1  # at least this cell counts

#             # continue in the same direction
#             dr, dc = dirs[d]
#             best = max(best, 1 + dfs(r + dr, c + dc, step + 1, d, turn_allowed))

#             # take one clockwise turn if allowed
#             if turn_allowed:
#                 new_d = (d + 1) % 4
#                 dr, dc = dirs[new_d]
#                 best = max(best, 1 + dfs(r + dr, c + dc, step + 1, new_d, 0))

#             return best

#         ans = 0
#         for r in range(ROW):
#             for c in range(COLS):
#                 if grid[r][c] == 1:
#                     # try starting in all 4 directions
#                     for d in range(4):
#                         ans = max(ans, dfs(r, c, 0, d, 1))
#         print(ans)
#         return ans


# obj=Solution()
# grid=[[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# obj.lenOfVDiagonal(grid)


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         check=[]
#         down=[]
#         out=True
#         k=0
        
#         rc_check=[]
        
#         def Center(r,c):
#             dr=[[-1,-1],[-1,0],[-1,+1],[0,+1],[+1,+1],[+1,0],[+1,-1],[0,-1],[0,0]]
            
#             for l,m in dr:
#                 if board[r+l][c+m]!='.':
#                     if board[r+l][c+m] not in rc_check:
#                         rc_check.append(board[r+l][c+m])
#                     else:
#                         print("twice",board[r+l][c+m],"r,c",r,c)
#                         return False
#             return True
                   
           
        
#         for i in range(len(board)):          
#             for j in range(9):
#                 if board[i][j]!=".":
#                     if board[i][j] not in check:
#                         check.append(board[i][j])
#                     else:
#                         print(board[j][i])
#                         out=False
#                         return out
                
#                 if board[j][i]!=".":
#                     if board[j][i] not in down:
#                         down.append(board[j][i])
#                     else:
#                         print(board[j][i])
#                         out=False
#                         return out
                    
#                 d=[[1,1],[1,4],[1,7],
#                     [4,1],[4,4],[4,7],
#                     [7,1],[7,4],[7,7]]   
                    
#                 if k<len(d):            
#                     if d[k]==[i,j]:
#                         if Center(i,j):
#                             k+=1
#                             rc_check=[]
#                         else:
#                             print("here")
#                             out=False
                        
                        
                
                    
            
#             check=[]
#             down=[]
    
#         return out
# obj=Solution()
# board =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# board=[[".",".",".",".","5",".",".","1","."],
#        [".","4",".","3",".",".",".",".","."],
#        [".",".",".",".",".","3",".",".","1"],
#        ["8",".",".",".",".",".",".","2","."],
#        [".",".","2",".","7",".",".",".","."],
#        [".","1","5",".",".",".",".",".","."],
#        [".",".",".",".",".","2",".",".","."],
#        [".","2",".","9",".",".",".",".","."],
#        [".",".","4",".",".",".",".",".","."]]
# board=[[".",".","4",".",".",".","6","3","."],
#        [".",".",".",".",".",".",".",".","."],
#        ["5",".",".",".",".",".",".","9","."],
#        [".",".",".","5","6",".",".",".","."],
#        ["4",".","3",".",".",".",".",".","1"],
#        [".",".",".","7",".",".",".",".","."],
#        [".",".",".","5",".",".",".",".","."],
#        [".",".",".",".",".",".",".",".","."],
#        [".",".",".",".",".",".",".",".","."]]

# board=[["5","3",".",".","7",".",".",".","."],
#        ["6",".",".","1","9","5",".",".","."],
#        [".","9","8",".",".",".",".","6","."],
#        ["8",".",".",".","6",".",".",".","3"],
#        ["4",".",".","8",".","3",".",".","1"],
#        ["7",".",".",".","2",".",".",".","6"],
#        [".","6",".",".",".",".","2","8","."],
#        [".",".",".","4","1","9",".",".","5"],
#        [".",".",".",".","8",".",".","7","9"]]
# obj.isValidSudoku(board)

# class Solution:
#     def sortVowels(self, s: str) -> str:
#         new=[]
#         result=""
#         count=0
#         char=["A","E","I","O","U","a","e","i","o","u"]
        
#         for j in range(len(s)):  
#             if s[j] in char:
#                 new.append(s[j])

                
                
#         new.sort()
        
#         print(new)
        
#         # for i in new:
#         #     print(ord(i),i)
#         # print(s)
        
#         for k in range(len(s)):
#             if s[k] in char:
#                 result+=new[count]
#                 count+=1
#             else:
#                 result+=s[k]
        
        
#         print(result)
#         return result
                
        
        
# obj=Solution()
# s="lEetcOde"
# obj.sortVowels(s)

# class Solution:
#     def maxFreqSum(self, s: str) -> int:
#         vowels=["a","e","i","o","u"]
#         v={"a":0,"e":0,"i":0,"o":0,"u":0}
#         c={}
#         result=0
#         for i in s:
#             if i in vowels:
#                 v[i]+=1
            
#             elif i in c:
#                 c[i]+=1

#             else:
#                 c[i]=1

#         if v and c:
#             result=max(v.values())+max(c.values())
#         elif v:
#             result=max(v.values())
#         elif c:
#             result=max(c.values())
            
#         print(result)
#         return result
            
    
    
# obj=Solution()
# s = "aeiaeia"
# obj.maxFreqSum(s)
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = []
        new_list = []
        
        # Precompute lowercase + devowel
        lower_map = {}      # lower -> first occurrence
        devowel_map = {}    # devoweled -> first occurrence
        exact_set = set(wordlist)

        def devowel(s: str) -> str:
            s = s.lower()
            for v in "aeiou":
                s = s.replace(v, "*")
            return s

        for w in wordlist:
            lw = w.lower()
            dv = devowel(w)
            new_list.append(dv)   # keep your original new_list usage
            if lw not in lower_map:
                lower_map[lw] = w
            if dv not in devowel_map:
                devowel_map[dv] = w

        def helper1(i):
            q = queries[i]
            if q in exact_set:         # exact match
                result.append(q)
                return 1
            lw = q.lower()
            if lw in lower_map:        # case-insensitive match
                result.append(lower_map[lw])
                return 1

        def helper3(i):
            dv = devowel(queries[i])
            if dv in devowel_map:      # vowel-error match
                result.append(devowel_map[dv])
                return 1

        for i in range(len(queries)):
            if helper1(i):
                continue
            elif helper3(i):
                continue
            else:
                result.append("")

        print(result)
        return result

                    
        
import time
start_time = time.perf_counter()

obj=Solution()
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
obj.spellchecker(wordlist,queries)
end_time = time.perf_counter()
execution_time = end_time - start_time

# Print the execution time
print(f"Execution time: {execution_time:.6f} seconds")