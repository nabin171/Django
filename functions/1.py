# def func():
#     a=int(input("Enter your number:"))
#     b=int(input("Enter your number:"))
#     c=int(input("Enter your number:"))
#     average=(a+b+c)/3
#     print(average)

# func()
# func()

# def goodday(argu,name="ram"):
#     print(f"nabin{argu}",name)

# a=goodday("hey")
# print(a)



# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)
# n=int(input("Enter the number"))
# print(f"the number is {factorial(n)}")\


#  write a program in python to find thte greatest of three numbers
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a=1
b=2
c=3

print("the greatest number is ",greatest(a,b,c))