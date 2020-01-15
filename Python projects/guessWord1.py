from random import *
l=["Red","Blue","Orange","Yellow","Pink"]
originalword=list(choice(l))
clen=len(originalword)
clenPlus1=clen+1
clenDiv2Plus1=(clen/2)+1
guess=[]
countunderscore=0
for i in originalword:
    if originalword.index(i)%2==0:
        guess.append("_")
        countunderscore+=1
    else:
        guess.append(i)
print(*([i for i in guess]))
turns=10
# while turns>0:
#     g=input("\nenter the alphabet to guess")
#     for i in range(0,clen):
#         if i%2==0:
#             if g in originalword:
#                 print(g,"is matched it is at location",originalword.index(g))
#             else:
#                 turns=turns-1
#                 print("you have left ",turns,"turns")


# for i in range(0,turns):
count=0
while turns>0:
    e=input("\nEnter alphabet to match")
    for j in range(0,clen):
        if j%2==0:
            if e.lower()==originalword[j].lower():
                guess[j]=e
                count+=1
                print(count,"items matched out of",countunderscore,"items")
                print(*[i for i in guess])
    turns=turns-1
    print("you have",turns,"turns")
    
    g=[i for i in guess]
    g="".join(g)
    og=[i for i in originalword]
    og="".join(og)

    if g.lower()==og.lower():
        print("Congratulations You won")
        break
    
if turns==0:
    print("you have failed")



