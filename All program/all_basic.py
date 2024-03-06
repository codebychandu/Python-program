
# a=10
# b=8
# print(a+b)

# c='chandu'
# d='kumar'

# print("hello world")
# print(18>74)

# print("a")
# print(a)
# print(id(a),id(b))
# print( c+" "+a)

# Arithmetic operator
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b) # 10*10*10

#assignment operator

# a=a+5
# print(a)

# a+=5
# print(a)

# a=a-b
# print(a)

# a-=b
# print(a)

#comparision operator

# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a>=b)
# print(a<=b)

#logical operator

# print(a==b and a>b) # both condition should be true
# print(a==b or a>b) # atleast one condition should be true
# print(not a!=b)  # it will give the opposite answer

#  Membership operator

# srring1 =  ' Hello world '
# print('h' in srring1)  # it will give false because python is case sentitive programming language
# print('h' not in srring1) 
# print('H' in srring1) 

# identity operator
# print(a is b , a==b)
# print(a is not b , a!=b)

# Bitwise operator
# print(bin(a))   # bin = binary value (bin is a function of binary value in python)
# print(bin(b))
# print(bin(a&b), a&b) # both true than true
# print(bin(a|b), a|b) # atleast one true than true
# print(bin(a^b), a^b) # for xor 0+0 or 1+1=0,   0+1 or 1+0=1

# ********************DATA TYPES*******************
# immutable data type
# 1)---> Numeric type
# c=23
# d=2.4
# e=2+3j
# print(c, type(c))  # a) integer 
# print(d, type(d))  # b) float
# print(e, type(e))  # c) complex

# 2)--> sequence type
# a) String

# c='i am a millinoaire'
# print(c, type(c))

# d="i am a millionaire"
# print(d, type(d))

# e='''
#    hello legend
#    i know, you are a millinioaire
# '''
# print(e,type(e))              # it will print as it is you wrote


#^^^^^^^^^^^^^^^^^^^^list^^^^^^^^^^^^^^^^^^^
# it is unordered data type, rounded with square bracket

# l=[1,2.3, 'good',12,261] # list any type of data it can store
# l[2]='nice'              # in list we can change(update) the value
# print(l,type(l))
        
            # little ADVANCE concept 
      #****List slicing*********
      
# l=[10,20,30,40,"hello"]
# print(l[1])
# print(l[3],l[4])
# print(l[1::5])
# print(l[1:])
# print(l[-1::-3])
      #****List iteration*****
# l=[10,20,30,40,"hello"]
# t=len(l)
# print(t)
# for i in range(t-1,-1,-1):
#  print(l[i])


#^^^^^^^^^^^^^^^^^^^TUPLE^^^^^^^^^^^^^^^^^^
# it is a ordered data type, rounded with perenthisis

# l=(12,2.4,"good")
# print(l,type(l))          # you can not change(update) the value in tuple like list
# l=(19)   # this line will show integer
# print(l,type(l))

#*******************Dictonary**************
# it is unordered key value pair, it's works on keys

# f={
#     'course_name':'python',
#     'duration_time':'2 months'
# }
# print(f['course_name'])
# print(f,type(f))

#***********SET************

# set is unordered collection of item, and every element will be unique , and you can change the set value

# g={1,2,2,3,2.3}
# print(g)

#*************TYPE CASTING ***********
#int, float, eval , input

# a=eval(input("enter the number"))  # eval = we can give integer,float and binary all type of value 
# b=eval(input("enter the number"))  # 10 = 0b1010
# print(a+b)

#************CONDITIONAL STEATMENT *****************

# 1) if statement
# 2) if else statement
# 3) if elif else statement

# a=int(input("enter a number:-"))
# if a%2==0:
#     print(a, "is even number")
# else:
#     print(a,"odd number")


#************MARKSHEET PROGRAM**************
# a=int(input("Enter your marks:-"))

# if a>80:
#     print("you are a toper")
# elif a>60:
#     print("fisrt division")
# elif a>33:
#     print(" second division")
# else:
#     print("you are FAIL")
#     print("Dont worry, try again")
# if a>33:
#     print("wel Done, keet it up!")

#**************CALCULATOR****************

# print(''' Guidence operator
# Add '+'
# substract '-'
# multiply '*'
# division '/'
# ''')
# a=int(input("Enetr the first number"))
# b=int(input("Enetr the Second number"))
# opr=input(" enter the ope...(+,-,*,/)")
# if opr=='+':
#     print(a+b)
# elif opr=='-':
#     print(a-b)
# elif opr=='*':
#     print(a*b)
# elif opr=='/':
#     print(a/b)
# else:
#     print("Invalid operator")

# ********for loop**********

# for i in range(5):
#     print(i)

# for i in range(2,11):
#     print(i)

# ******TABLE*******
# for i in range(2,21,2):
#     print(i)
#for i in range(1,11): 
#    print(1*i,'  ',2*i,'  ',3*i,'  ',4*i, '  ',5*i)

#***REVERSE FOR LOOP

# for i in range(11,-5,-1):
#    print(i)

#*****while loop********

# i=1
# while i<=10:
#     print(i)
#     i+=1

# *********String Slicing********

# c="i am a programmer"
# print(c[5])
# print(c[0:1])
# print(c[0:15:2])
# print(c[-1::-1]) # for reversce

#******String iteration********
# c="i am a programmer"
# c=c[-1::-1]
# a=len(c)
# print(c)

# for i in range(a): #a=18
#     print(c[i])

# for i in range(a-1,-1,-1):
#     print(c[i])

#***python string function*******
# 1) lower()
# 2) upper()
# 3) title()
# 4) capitalize()

# a="I Am A Good Programmer"
# b=a.lower()
# print(b)
# e="i am a good programmer"
# f=e.upper()
# print(f)
# g=e.title()
# print(g)
# h=e.capitalize()
# print(h)

#**********String function**************
# 1) find()
# 2) index()
# 3) isalpha()
# 4) isalnum()
# 5) isdigit()

# c="programmer"
# # # both function will find index number from the string
# # print(c.find('z')) # this line will print -1
# # print(c.index('z')) # this will give error
# print(c.isalpha()) # only for alphabate number
# print(c.isdigit()) # only for number
# print(c.isalnum()) # for both alphabate and number

# chr()  : integer to character
# ord()  : character to integer 
# a=65
# print(chr(65))
# b="A"
# print(ord("A"))

# a="I Am A Good {} {} Programmer".format("boy","and")
# print(a)
# a="I Am A Good {0} {1} Programmer".format("boy","and")
# print(a)
# a="I Am A Good {a} {b} Programmer".format(a=5,b=7)
# print(a)

#**************list function**********

# 1) del
# 2) pop()
# 3) remove()
# 4) clear()
# 5) update()  #not add it will update the value
# 6) insert()  # add the value at any point
# 7) append() # add as it is with bracket
# 8) extend()  # add as it is but in the last


# l=[10,20,30,40,50]
# # # del l[1]   # just delect
# # # print(l)
# # print(l.pop(3))
# # print(l)  # IT can print pop(delected) value
# # l.remove(10)
# # print(l)
# l[0]=10
#print(l)
# l.clear()  #delect all value
# print(l)

# p=[20,40,60,80]
# # p.insert(0,10)
# # print(p)
# # first way for append
# # p.append(50) 
# # print(p)

# #second way
# # n=[70,80]
# # p.append(n)
# # print(p)n

# n=[40,50]
# p.extend(n)
# print(p)

#********LIST COMPRIHENTION*********

# l=[]
# for i in range(1,101):
#  l.append(i)

# print(l)
# n=[h for h in range(1,101) if h%2==0]
# print(n)

# s ="hello"
# d = [g for g in s]
# print(d)

# ********List function*******
# count()
# max()
# min()
# sort()
# reverse()
# index()

# l= [10,20,30,40,50,20,30]
# a=l.count(20)
# print(a)
# m=max(l)
# print(m)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# b=l.index(10)
# print(b)

#******ZIP function******
# l1=[10,20,30,40]
# l2=[20,30,40,50]

# t=len(l1)

# # first way

# for a,b in zip(l1,l2):
#    print(a,b)
#  # second way
# for i in range(t):
#  print(l1[i],l2[i])

#*********String to list********

# a="i am a programmer"
# print(a)
# l=a.split()
# print(l)

#for many value
# l=[]
# for i in range(1,4):
#     n=input("enter the value"+str(i)+":-")
#     l.append(n)
# print(l)            # here space can change the value

##*****Dictonary******

# d={
#     'name':'chandu',
#     'rollno':'97',
#     'duration': '4 years'
# }
#  print(d)
# first way
# f=d['name']
# print(f)

# second way
# for n in d:
#     print(d[n])

# **Dictonary function****
# 1 get()    :- you can get the value from the dictonary
# 2 key()    :- you will get all keys value
# 3 value()  :- you will get the values from the dictonary
# 4 item()   :- yoy can get keys and value both
# 5 del      :- del is a keyword not a  function
# 6 pop()    :- remove the element from the dictonary
# 7 dict()   :- it is a dictonary 
# 8 update() :- update the value
# 9 clear()  :- delect all the dict value

# c=d.get("name")
# print(c)
# for a in d.keys():
#     print(a)
# for a in d.values():
#      print(a)
# for a,b in d.items():
#     print(a,b)
# del d['name']
# print(d)
# print(d.pop('duration'))
# print(d)
# d=dict(name='chandu',fees=4000)
# print(d)
# d.update({'fees':1000})
# print(d)
# d.clear()
# print(d)
# d['course']='python'  # for update the value
# print(d)

#****Nested dictonary*****
# course={
#       'php':{'duration':'3 month','fees':15000},
#       'java':{'duration':'2 month','fees':10000},
#       'python':{'duration':'4 month','fees':12000}

#  }
# print(course)
# print(course['php']['fees'])

# for a,b in course.items():
#     print(a,b)

#********Tuple*****

# t=(12,13,14)
# print(t)

#Function
# min()
# max()
# count()
# Index()
# sum()

# m=min(t)
# print(m)
# c=t.count(12)
# print(c)
# i=t.index(14)
# print(i)
# s=sum(t)
# print(s)
#********SETS*****

# s={10,20,30}
# print(s)
# print(type(s))
# for a in s:
#     print(a)

#******SETS function******

# set() :- convert list or tuple to set
# add()
# pop()
# remove()
# clear()
# discart()
# update()

# l=[10,20,30,'hello']
# s=set(l)
# print(s)
# s.add(70)
# print(s)
# s.pop()
# print(s)
# s.remove(10)
# print(s)
# s.discard(20)
# print(s)
# s.clear()
# print(s)

# s={10,20,30,40}
# l=[50,60,70]
# s.update(l)
# print(s)


#****USER DEFINE FUNCTION****
# NOTE :- there is two thinks first define the func and second call the func that's all

# def firstprogram():
#     print("my first function program")

# firstprogram()

# program of sum from function
# def sum(a,b):
#     print(a+b)

# n1=10
# n2=20
# sum(n1,n2)

# return func
# def sum(a,b):
#     c=a+b
#     return c

# n1=10
# n2=20
# output=sum(n1,n2)
# print(output)

# n1=13
# n2=15
# output=sum(n1,n2)
# print(output)
# def mul(a,b):
#     c=a*b
#     return c;

#***Default parameter value***
# def sum(a,b=5):
#     print(a+b)

# sum(23)  # "b" value take automatically

#**retuen value***
# return value use for store the data. if you don't want to print the value .
#than just you can store the data in the return value, without print func it will not give the output

# def square(x):
#     return x*x
# s=square(5)
# print(s)

#**************Math module function*************
# import math

# x=12.1
# print(math.ceil(x))    # ceil will give you next integer no, it will not work on integer no, need float value

# x=-14
# print(math.fabs(x))  # fabs will give positive float value, for integer you can use abs with ',' 
# x=5
# print(math.factorial(x))

# x=12.7
# print(math.floor(x))  # floor will give previous value

# l=[10,29,43,42,65]
# print(math.fsum(l)) # fsum will add the all list value and it will provide float no

# print(math.sqrt(15))  #you can fine square root

#***********Random module function*************

# import random
# print(random.randint(1,10)) # any value will come between 1 to 10
# print(random.randrange(2,4)) # it never give value 4

# l=[10,20,30,40,50,60]  # any value will give from list through random.choice
# c=random.choice(l)
# print(c)

# r=random.random() # any float value well give between 1 and 0
# print(r)

# l=[10,20,30,40,50,60]
# random.shuffle(l)   # shuffle the list value
# print(l)

# u=random.uniform(2,9)  #random.uniform will give any float value between range
# print(u)

#*********Datetime module function********

# import datetime

# d=datetime.datetime.now()
# m=d.strftime("%Y")     # %y, %Y=years, %b, %B, %m, %H=hours, %i=in 12 hours, %p=pm/Am, %m= minuts, %s=seconds
# print(d)
# print(m)

#************PICKLE library*************
# pickle can wrire the in diffrent/ another file
# it have two method dump() and  load()
# you can picle object with following data types
# booleans,
# integers,
# float,
# complex number,
# (normal and unicode) string
# tuple ,
# list,
# sets 
# dictonary,


#dump()= you can write the value
# import pickle
# l=[10,20,30,40,50]
# file=open("write.txt","wb")
# pickle.dump(l,file)
# file.close()

#load()= you can read the value
# import pickle
# file=open("write.txt","rb")
# l=pickle.load(file)
# print(l)

#**********JSON (javascript object notation) *********
# it's mainly use for  storing and transfering data between browser and server

# import json
# d='{"course":"python","duration":"2 months","fees":"4000"}'

# x=json.loads(d)
# print(type(x))
# print(x)
# for a in x:
#     print(a,x[a])

#********object oriented programming********
#********inheritance*********
# super()
#@getters() and @sctters()
#overloading and overriding
#overloading👇


# class Area:
#       def find_area(self,x=None,y=None):

#             if x!=None and y!=None:
#                   print(x*y)
#             elif  x!=None:
#                   print(x*x)
#             else:
#                   print("NOTHING...")

# obj1=Area()
# obj1.find_area()
# obj1.find_area(10)
# obj1.find_area(10,20)

# u=int(input("Enter the number"))
# for i in range(1,11,1):
#       match i:
#             case i:
#                   print(u*i)



#^^^^^^^^^^Extra part^^^^^^^^^^^^^^^^^^

# from kivy.app import App
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):
#      label = Label(text="this is my first app using python")
#      return label


# MyApp().run()