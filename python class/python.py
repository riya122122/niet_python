'''print("Hello #World")'''

'''a,b = input(),input()
print(a)
print(b)'''

'''a,b = input("Enter 1st number"),input("Enter 2nd number")
print(a,b)'''

'''a = 10
print(type(a))'''

'''print("Hello World"*5)'''

'''
print("Hello World\n"*5)
'''

'''a,b,c = float(input("enter 1st side")),float(input("enter 2nd side")),float(input("enter 3rd side"))
print("perimeter of triangle:",float(a+b+c))'''

'''a = int(input("Enter the  1st number"))
b = int(input("Enter the 2nd number"))
print("sum is:",a+b)
print("subtract is:",a-b)
print("multiplication is :",a*b)
print("divide is:",a/b)
print("floor is:",a//b)
print("modulus is:",a%b)
print("exponential is:",a**b)'''

'''# f to c
f = float(input("Enter the degree in fehrenheit"))
c =  (f-32)*5/9
print("the celcius of a given fehrenheit:",c)'''

'''# c to f
c = float(input("Enter the temperature in celsius"))
f = (c*9)/5+32
print("the fehrenheit of a given celsius:",f)'''

'''a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if a>b:
    print("the 1st number is greater:",a)
else:
    print("the 2nd number is greater:",b)'''

'''a = int(input("Enter a number"))
if (a>0):
    print("number is positive")
else:
    print("number is negative")'''

'''a = int(input("Enter a number"))
if (a%2==0):
    print("number is even")
else:
    print("number is odd")'''

'''a = float(input("Enter the number"))
last_digit=a%10
print("the last_digit is:",last_digit)'''



'''a=int(input("enter the number of maths"))
b=int(input("enter the number of phy"))
c=int(input("enter the number of os"))
d=int(input("enter the number of ds"))
e=int(input("enter the number of pc"))
sum=maths+phy+os+ds+pc
pert=sum*100/500
if(pert <= 40):
    print("grade E")
elif(pert > 40 and 60 >= pert):
    print("grade D")
elif(pert > 60 and 70 >= pert):
    print("grade C")
elif(pert > 70 and 90 >= pert):
    print("grade B")
else:
    print("grade A")'''

'''age = int(input("Enter the age"))
if(age<=13):
    print("child")
elif(age>14 and age<=19):
    print("teenage")
elif(age>20 and age<=60):
    print("adults")
else:
    print("senior citizens")'''



'''num = int(input("Enter number"))
if(num>=0):
    if(num==0):
        print("zero")
    else:
        print("positive")
else:
    print("negative")'''

'''print("calculator")
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
sym = int(input("what do you want to do"))
if (sym==1):
    print("addition is:",1)
if (sym==2):
    print("subtraction is:",2)
if (sym==3):
    print("multiplication is:",3)'''



'''year = int(input("Enter a 4 digit year:"))
if (year%4==0 and year%100!=0)or(year%400==0):
    print("This is a leap year:",year)
else:
    print("This is not leap year:",year)'''


'''a = "Riya"
print("{} likes dance".format(a))'''


'''Student_id = 45689
name = 'Riya'
print("Student name is {}.\nStudent id is {}".format(Student_id,name))'''

'''a = 'Riya'
b = 21
c = 'orai'
print("My age is {1}.\nMy name is {0}.\nI live in {2}".format(a,b,c))'''
      


'''a = 5678.3437783979
print("{:.3%}".format(a))
print("{:.4%}".format(a))
print("{:.11%}".format(a))'''

'''
#loops
for i in range(10):
    print((i+1)*2)
'''

'''for i in range(10):
    print("2 X",i+1,"=",(i+1)*2)'''



'''a = 0
b = 1
for i in range(10):
    print(a)
    next_number = a+b
    a = b
    b = next_number'''


'''i = 1
while i<=10:
    print((i)*2)
    i=i+1'''
    

'''for i in range(10):
    if(i==8):
        continue
    else:
        print(i)'''


'''for i in range(10):
    if(i==6):
        break
    else:
        print(i)'''

'''for i in range(20):
    if(i%2!=0):
        continue
    else:
        print(i+2)'''

'''for i in range(1,21):
    if(i%2!=0):
        continue
    else:
        print(i)'''

'''for i in range(5):
    for j in range(5):
        print(end = "")
    print(i)'''


'''for i in range(5):
    for j in range(i+1):
        print(i+1,end ="")
    print()'''

'''rows = 5
for i in range(rows+1):
    for j in range(i):
        print(i,end="")
    print()'''


'''for i in range(4+1):
    for j in range(i+1):
        print(i+1,end="")
    print()'''



'''def sum_number():
    a = 20
    b = 34
    print(a+b)
sum_number()'''


'''def sum_number():
    a = int(input())
    b = int(input())
    print(a+b)
sum_number()'''

#1st type
'''def fibonacci_series():
    a = 0
    b = 1
    for i in range(10):
        print(a)
        res = a+b
        a = b
        b = res
fibonacci_series()'''


#2nd type
'''def sum_number():
    a = 6
    b = 89
    c = a+b
    return c
d = sum_number()
print(d)'''



#3rd type
'''def add(a,b):
    print(a+b)
add(45,78)'''


'''def add(a):
    b=5
    print(a+b)
add(34)'''

#4th type
'''def add(a,b):
    c = a+b
    return c

print(add(10,5))'''


'''def add(a,b,c=23):
    d = a+b+c
    return d
e = add(6,8)
print(e)'''


'''def add(a,b=6):
    c = a+b
    return c
d = add(5,4)
print(d)'''

#recursion
'''def fun(n):
    if n==1:
        return 1
    return n*fun (n-1)
print(fun(5))'''

#modules
'''import calender
from calender import *'''


'''from datetime import date
date1 = date(2023,4,14)
print("Date:",date1)
print("year:",date1.year)
print("month:",date1.month)
print("day:",date1.day)
print(dir(date))'''

'''from datetime import datetime
dt = datetime.now()
print(dt)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dir(dt))'''


'''import calendar
print(calendar.calendar(2025))
print(dir(calendar))'''










        

      


    




 

        



