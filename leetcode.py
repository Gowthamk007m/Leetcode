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

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS,COLUMS=len(matrix),len(matrix[0])
        cache={}
        
        def helper(r,c):
            if r>=ROWS or c>=COLUMS:
                return 0
            
            if (r,c) not in cache:
                down=helper(r+1,c)
                right=helper(r,c+1)
                diag=helper(r+1,c+1)

                cache[(r,c)]=0
                
                if matrix[r][c]=="1":
                    cache[(r,c)]=min(down,right,diag)+1
                    

            return cache[(r,c)]
        helper(0,0)
        print(max(cache.values())**2)
        return max(cache.values())**2
        



obj=Solution()
matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
obj.maximalSquare(matrix)

matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]