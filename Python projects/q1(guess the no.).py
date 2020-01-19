# #1 to 20 guess no
# from random import *
#
# ls=list(range(1,21))
# print(ls)
#
# ran=randint(1,20)
# c=0
#
# s=int(input("enter a number "))
# while(s!=ran):
#     if s<ran:
#         print("no. is low try again")
#         s=int(input("enter a number "))
#         c=c+1
#
#
#     elif s>ran:
#         print("no. is greater try again")
#         s = int(input("enter a number "))
#         c = c + 1
# print("matched")
# c=c+1
# print("random no:",s)
# print(c)
#


#sir ka logic

from random import *

ran=randint(1,20)
c=0
for i in range(1,21):
    n=int(input("enter no. to match"))

    if(n==ran):
        print("matched")
        break
    elif n<1 or n>20:
        print("plz enter between 1 to 20")
    elif n>ran:
        print("to high")

    elif n<ran:
        print("to low")

    c=c+1
c=c+1
print("random no. is:",ran)
print("count:",c)

