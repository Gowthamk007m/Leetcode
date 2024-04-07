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

def checkValidString(s):
    """
    :type s: str
    :rtype: bool
    """
    