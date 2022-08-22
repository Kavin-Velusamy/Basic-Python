### DSA in python

# stack
# LIFO (last in first out)
# methods
# push ,pop, peek ,contain

# push
# size=0
# stack.push("a")      # adding one element                     
# size=1                                                        c         third 
#  stack.push("b")      # adding second  element                b       second
# size=2                                                        a    we are adding first element
# stack.push("c")      # adding third element                2323434    this is base element
# size=3 

# pop              # pop means it removes the first element
# size=3
# stack.pop()     # in pop  we added  element
# return =c       # we remove one element ,it returns c
# size=2
# stack.pop()     # in pop  we added second  element
# return =b       # we remove one element ,it returns b
# size-1
# stack.pop()     # in pop  we added three element
# return =a       # we remove one element ,it returns a
# size=0

# peek
# it will not change the element
# size =3
#return c

# contain
# it will find the element 
# stack.contain("c")
# return= true
# stach.contin("d")
# return= false
# size=3

# push and pop

# stack=[]                ##### code
# stack.append(10)      # push
# stack.append(20)
# stack.append(30)
# stack.append(40)
# # print(stack) 
# # stack.pop()        # pop
# # print(stack)
# # stack.pop()
# # print(stack)
# # stack.pop()
# # print(stack)
# # stack.pop()
# # print(stack)
# print(stack[-2])    # it will remove in last
# print(stack[-1])

# stack=[]              # this stack is empty
# print(len(stack)==0)    # 0 is empty means true
# print(stack)

##Stack using list

# stack=[]
# def push():
#     #  if len(stack)==n:
#     #      print("List is full")
#     # else:
#         element=input("Enter the element:")
#         stack.append(element)
#         print(stack)
# def pop_element():
#     if not stack:
#         print("stack is empty")
#     else:
#         e=stack.pop()
#         print("removed element",e)
#         print(stack)
#  ##n=int(input("Enter the limit"))        # this step for limit in stack 
# while True:
#     print("Selected the operation 1.push 2.pop 3.quit")
#     choice=int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         break
#     else:
#         print("Enter the correct operation")

## stack using modules

# import collections
# stack=collections.deque()
# print(stack)
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# print(stack) 

# ## ARRAY in qt
# # ###
# # n=int(input("Enter the limit :"))
# # a=[]
# # print("Enter the number")
# #for i in range(n):
# #     a.append(input())
# # for i in range(n):
# #     print("a[",i,"]=",a[i])

# ###sum of element in array

# n=int(input("Enter the Limit:"))
# a=[]
# sum=0
# print("Enter the element")
# for i in range (n):
#     a.append(int(input()))

# for i in range(n):   
#     sum+=a[i]
# print("sum of array",sum)
    
    
### Queue 
### First in First out(FIFO)
### Last in last out (LILO)
## enqueue = adding the element in first queue
## dequeue = removing the element in first  queue

# queue=[]
# queue.append(10)
# print(queue)
# queue.append(50)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# print(queue)
# queue.pop(0)      ## we want to give the index
# print(queue)
# queue.pop()       ## this will remove in last element
# print(queue)
                
##enqueue
# queue=[]
# queue.insert(0,10)
# queue.insert(0,20)
# queue.insert(0,30)
# print(queue)

### queue using list

# queue=[]
# def enqueue():
#     element=int(input("Enter the element :"))
#     queue.append(element)
#     print(element,"is added in the queue")
# def dequeue():
#     if not queue:
#         print("queue is empty")
#     else:
#         e=queue.pop(0)
#         print(e,"removed element")
# def display():
#     return queue

# while True:
#     print("select the operation 1.add 2.remove 3.show 4.quit")
#     choice=int(input())
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     elif choice==3:
#         display()
#     elif choice==4:
#         break
#     else:
#         print("Enter the correct operation")

# ## queue usind class

# import collections
# q= collections.deque()
# print(q)
# q.append(10)
# q.append(20)
# q.append(30)
# q.append(40)
# print(q)
# q.pop()
# print(q)
# q.pop()
# print(q)


''''''
# # class array_queue:
#     def __init__(self):
#         self.capacity=10
#         self.size=0
#         self.data=[None]*4

#     def len (self):
#         return self.size()

#     def _isempty (self):
#         return self.size==0

#     def enqueue (self,element):
#         element=int(input("Enter the number"))
#         self.append(element)
''''''

### Bubble Sorting

# a,b=3,6           ### ex simple method
# print(a)
# temp=a
# a=b
# b=temp
# print(a,b,temp)

### Bubble sort

# def bubble_sort(nums):
#     for i in range (len(nums)-1,0,-1):
#         for j in range (i):
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp
        
# nums=[5,3,8,9,1,0,7]
# bubble_sort(nums)
# print(nums)

## method of bubble sort 

# def bubble_sort(self,list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-1):
#             if list[j]>list[j+1]:
#                  temp=list[j+1]
#                  list[j+1]=list[j]
#                  list[j]=temp

# list=[3,5,2,8,1,9]
# bubble_sort(list)
# print(list)

# ### Selection sort

# def sort(nums):
#     for i in range(5):
#         minpos =i
#         for j in range(i,6):
#             if nums[j]<nums[minpos]:
#                 minpos=j
#         temp=nums[i]
#         nums[i]=nums[minpos]
#         nums[minpos]=temp

# nums=[5,3,8,6,7,2]
# sort(nums)
# print(nums)

##code of selection sort
#  
# for i in range(5):
#         minpos =i
#         for j in range(i,6):
#             if min[j]<min[minpos]:
#                 minpos=j
#         temp=min[i]
#         min[i]=min[minpos]
#         min[minpos]=temp
 
# ### Insertion Sort

arr=[4,2,7,8,5,45]

for i in range (len(arr)):
    cur=arr[i]
    for j in range (i-1,-1,-1):
        if arr[j]>cur:
            arr[j+1]=arr[j]
        else:
            arr[j+1]=cur
            break
for i in range (0,len(arr)):
    print(arr[i],end=' ')       



