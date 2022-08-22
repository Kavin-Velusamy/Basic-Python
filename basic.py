###Basic of python


# int=3534654
# string="any value" (Double arrow mark)
# float=34.44     #decimal value
# List=[" "]      #list inside string
# Tuple=()
#boolean=true,false

#String=Tuple= immutable(we cannot change the value)
#List= mutable 


##variable 

# print ("hello world")    # print()- inbulit function
# name="kavin22012004"     # name= variable (we can store the values)  # string ("set of character")-command 
# print("Hi" + name)
# name="john" 
# print ("hi",name )
# price=45
# amount=34.5             #float value
# child = False           #booleam
# print(child)
# print(price)


###string handling

# code="python learning"
# work="'string'"
# name="in github"
# print(work)     
# # print(code.upper())         # fully captial letter 
# print(code.lower())         #fully small letter
# print(code.capitalize())    #first letter capital
# print(code.title())         #firat letter and space after the letter is capital
# print(code +" " + name + work)   #connecting the words or numbers
# print(code+" "+name)        #space of the words
# print("python \nlearning")    #this will print in next line
# print("python \t learning") #giving the the double space of the words
# print(code.isupper())        #if all the letter is upper(true)
# print(code.islower())        #if all the letter is lower ()
# print(len(code))             #finding the index of the word
# print(code.find("n"))        #finding the letter (n)
# print(code.count("n"))      #counting the letter (n)
# print(code.replace("a","s")) #replacing the words
# print(code.isalpha())        #finding all the the letter is alpha letter
# print(code.isdigit())
# print(code*5 )              


# ## multiple assignment in single line

# name,age ,weight="kavin",19,52    #types of variable in one line
# print(weight)
# like=dislike=65
# print(dislike) 
# print(like/dislike)
# print(like*dislike)


###Type casting

#otp=3252363
#otp=str(otp)     #type casting
#print("Your otp is" + str(otp))
#print(type(otp))
#count,number=199,"199"
#print(count+1)
# #count="199"
# print(number+"1")

##Assignment 1
# name="Anand"
# leave="15 days"
# year=2021
# print(name,leave,year)

###Assignment 1               #This is correct method
###Dear Anand,
###You have 15 days of Leave Balance for this
###Year(2021)
# name, leave, year ="Anand",15,2021
# print("Dear " + name + ",\nYou have " + str(leave) + " days of Leave Balance for this\nYear("+ str(year)+")")

# name, leave, year ="Anand",15,2021      #### this code is space error beacuse of (,) this  kama
# print("Dear " , name , ",\nYou have " , str(leave) , " days of Leave Balance for this\nYear(", str(year),")")


### Getting the input from the user

# name=input(" Enter your name:")
# print("Hello"+ name)
# height=float(input("Enter the height:"))
# print(type(height))
# height="{:.4f}".format(height/2.54)     ##{} this is for after the float value, 2 digit {:.2},4 digit {:.4}
# print("Your height is "+ str(height) + "cm")
# #print("Your are " + str(height/2.54) + "inches")
# print("Your are " + height + " inches tall")


###Assignment 2
 
# ## Get user input
# ## Name,Email ID and phone number.print the information like this
# ##  ****************************
# ##  UserName: XXXXX
# ##  Email   : XXXXX
# ##  ph      : XXXXX
# ##  ***************************

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")
 
# print("*****************************")

# print("UserName:",Name)
# print("Email :",Email)
# print("Ph :",Phoneno)

# print("*****************************")


# ## This is another type of code 
# ## Assignment 2

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")

# print("*****************************")

# print("UserName :" + Name + "\n   Email :" + Email + "\n      Ph :" + Phoneno )

# print("*****************************")


### Math operation

# a=20
# b=10
# print(a+b , a-b , a*b , a/b , a/50 , b/30 , (a+b)*40 , a+b*30)      ##give output in float (/) division
# print(10/2 , 20*3)
# a=23.5
# print(round(a))      # round is the absolute correct answer
# a=-5
# print(abs(a))        # ABS is the absolute value of a
# a=5
# print(abs(a))
# print(pow(a,4))      # pow is the power of a
# print(a**4)          # this is another mothod of power term
 
# a=55
# b=32
# print(max(a,b))       # maximum value of a,b
# print(min(a,b))       # minimum value of a,b
 
# import math  # math module
# a=45.6
# print(math.ceil(a))    # ceil is the decimal value of a=5
# print(math.floor(a))   # floor is the decimal value of a=4
# print(math.factorial(9))   # factorial of 9
# a=6
# print(a%2)       # it will find the remainder
# print(a%5)
# print(a%9)

### Assignment 3

## Get user input 
## Get the number n fron user.compute and print the follwoing values
## 1.log2(n)
## 2.cos(n)
## 3.e**n

# # print(math.log2(16))
# # print(math.cos(16))
# # print(math.e**16)
# m=input("User input :")
# n=int(m)
# print("1.",int(math.log2(n)), "2.",int(math.cos(n)),"3.",int(math.e**n))


 ### If Else (true/False)conditional 
 
# pwd_correct= True
# if pwd_correct:        #conditional statement
#     print("logged in")
# else:
#     print("incorrect pwd")

## Relational operator

# num=35
# if num<30:            # < lower number           #  == is it equal
#     print("true")     # > higher number          #  != is it not equal
# else:                 # <= same number or lower number
#      print("false")   # >= same number or higher number 

# num=14
# if num%5==0:       # it is divisible by 5 means ,print true
#     print("Multiple of 10")
# else:
#     print("Not multiple of 10")

##Elif ladder

# ind_score=150
# if ind_score>=150:
#     print("india won")
# elif ind_score>=100:
#     print("pak win")
# elif ind_score>=90:
#     print("Aus win")
# else:
#     print("jap win ")

## Nested if

# #check if the number is three digit number                      # A     B    And       OR     NOT
# #logical operation -and (or) or      # this method is 'and'
#                                                                  T     T     T        T       0 = 1
# num= int(input("Enter the number :"))                          # T     F     F        T       1 = 0
# if num>99 and num<1000 :                                       # F     T     F        T
#     if num%2==0:                                               # F     F     F        F
#         print(str(num),"is the three digit number")
# else:
#     print(str(num) ,"is not a three digit number")  

##This method is OR
# name="kavin"
# if name[0]=="k" or name[0]=="K":
#     print("the name starts with s")


###Bitwise operator
## And , OR , Not , Exor , Leftshift , Rightshift
#  left shift                                                 # Exor
#  00001100 12<<1    it will leave the first no                  # a^b
#  00011000 =24                                                  #  0 0 =0
# Right shift                                                    #  1 0 =1
# 00001100   12>>1                                               #  0 1 =1
# 00000110 = 6                                                   #  1 1 =0


###String slicing

# name="kangani patti"
# print(name[9])              #this will print the index value
# print(name[0:7])
# print(name[2:11])
# print(name[1:12:2])       # this will print one after another value
# print(name[-4])          # this will print in back side
# print(name[::-1])
# print(name[2:-2])
# x=slice(2,-2)
# print(name[x])

####Assignment 4
#str="Happy"
# H                 y
# Ha                py
# Hap               ppy
# Happ              appy
# Happy             Happy

# print("H          "+"y")
# print("Ha         "+"py")
# print("Hap        "+"ppy")
# print("Happ       "+"appy")
# print("Happy      "+"Happy")
# str="Happy"
# print(str[0])
# print(str[:2])
# print(str[:3])
# print(str[:4])
# print(str[:5])
# print(str[-1])
# print(str[-2:])
# print(str[-3:])
# print(str[-4:])
# print(str[-5:])


###List

# cities=["chennai","madurai","thricy" ,"coimbatore","salem"  ]
# val=[1,5,8,5,4,7]
# list=["salem",3 ,"namakkal"]
# print(list[2])
# print(val[4])
# print(cities[3])
# print(cities[:4])
# print(val[-4])
# print(cities)
# cities[2]="Thrichy"         # this will change the letter
# print(cities)      
# cities.append("sivakasi")    #inserting the element in last
# print(cities)
# cities.insert(2,"karur")     # inserting the element inside the place
# print(cities)
# delete=cities.pop()         # this will delete the last element and also say which element is deleted
# print(delete,"has been deleted")
# print(cities)
# del cities[2]             #this will delete the element
# print(cities)
# cities.remove("salem")   # we are giving the place to delete
# print(cities)
# print(sorted(cities))    # this will print in accending order
# print(sorted(val))
# cities.sort()         # this is also sorting  
# print(cities)
# cities.reverse()
# print(cities)       #  we can find how many value in list 
# print(len(cities))


###While Loop

# letter=' '
# while letter.isalpha():
#  letter= input("enter the alphabet:")
# print("You have entered "+letter)

##To print 1 t0 100
# num=0
# while num<=99:
#   num+=1
#   print(num,end=',')


### For loop

# for i in range (1,100):
#     print(i,end=',')

# list=[22,456,34234,566,345]
# for i in list:
#     print(i*i)

# string=(2,35,"kavin",34,556)
# for i in string:
#     print(i)


### simple Game
### I am chossing the number below 10
### reandomly I am chosing any number
### its correct it will print
### its wrong try again

import random
n=input("enter the limit:")
num=random. randint(1,10)
guess=int(input("can u guess the no I am thinking "))
while num!=guess :
    if len(guess)==0:
        print("list is full")
    if guess>num:                                                              ### dout
        print("your guess is higher")
    else:
        print("your guess is lower")
        guess=int(input("try again :"))
print("you won") 


### Assignment 

##1.Get input number n from user. print all the factor of n
##2. Get a list of to do task from the user and add it to a to_do list.print the list
##3.Given an array of intrgers.find a peak element in it .An array element is the peak if it is NOT samller than its neighbours.
## For corner element ,we need to consider only one neighbour.  Eg in..[3,4,6,7,5] -7 is a peak element.
##4.List=[3,4,5,-2,-1,2,8,0,-4].Move all negative number to the end of list.





