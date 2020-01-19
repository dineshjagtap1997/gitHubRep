from random import *
def draw_man(stage):
    one=("___________")
    two=("| /{}")
    three=("|/{}")
    four=("|{}")
    five=("|{}")

    if stage==0:
        print(one)
        print(two.format(" "))
        print(three.format(" "))
        print(four.format(" "))
        print(five.format(" "))
    if stage==1:
        print(one)
        print(two.format(" |"))
        print(three.format(""))
        print(four.format(" "))
        print(five.format(" "))
    if stage==2:
        print(one)
        print(two.format(" |"))
        print(three.format("  O"))
        print(four.format(" "))
        print(five.format(" "))
    if stage==3:
        print(one)
        print(two.format(" |"))
        print(three.format("  O"))
        print(four.format(" --|--"))
        print(five.format(" "))
    if stage==4:
        print(one)
        print(two.format(" |"))
        print(three.format("  O"))
        print(four.format(" --|--"))
        print(five.format("  /\\"))

l = ["Red", "Blue", "Orange", "Yellow", "Pink"]
originalword = list(choice(l))
clen = len(originalword)
clenPlus1 = clen + 1
clenDiv2Plus1 = (clen / 2) + 1
guess = []
countunderscore = 0
for i in range(clen):
    if i % 2 == 0:
        guess.append("_")
        countunderscore += 1
    else:
        guess.append(originalword[i])
print(*([i for i in guess]))
turns = 10


# for i in range(0,turns):
count = 0
draw=0
draw_man(draw)
while turns > 0:
    e = input("\nEnter alphabet to match")

    # for j in range(0, clen):
    #     if j % 2 == 0:
    #         if e.lower() == originalword[j].lower():
    #             guess[j] = e
    #             count += 1
    #             print(count, "items matched out of", countunderscore, "items")
    #             print(*[i for i in guess])
    o=[i for i in originalword]
    o="".join(o).lower()


    if e.lower() in o.lower():
        print("match")
        g1=o.index(e)
        guess[g1]=e
        print(*[i for i in guess])
    else:
        draw+=1
        draw_man(draw)
        turns = turns - 1
        print("you have", turns, "turns")

    g = [i for i in guess]
    g = "".join(g)
    og = [i for i in originalword]
    og = "".join(og)

    if g.lower() == og.lower():
        print("Congratulations You won")
        break
    if draw==4:
        turns=0
if turns == 0:
    print("you have failed")














# import os
# import time
#
# def draw_man(stage):
#
#     one = (" ________")
#     two = (" | / {}")
#     three = (" |/ {}")
#     four = (" | {}")
#     five = (" | {}")
#     six = ("___|____")
#
#     if stage == 0:
#
#         print(one)
#         print(two.format(" "))
#         print(three.format(" "))
#         print(four.format(" "))
#         print(five.format(" "))
#         print(six)
#
#     if stage == 1:
#         print(one)
#         print(two.format("|"))
#         print(three.format(" "))
#         print(four.format(" "))
#         print(five.format(" "))
#         print(six)
#
#     if stage == 2:
#         print(one)
#         print(two.format("|"))
#         print(three.format("O"))
#         print(four.format(" "))
#         print(five.format(" "))
#         print(six)
#
#     if stage == 3:
#         print(one)
#         print(two.format("|"))
#         print(three.format("O"))
#         print(four.format("--|--"))
#         print(five.format(" "))
#         print(six)
#
#     if stage == 4:
#         print(one)
#         print(two.format("|"))
#         print(three.format("O"))
#         print(four.format("--|--"))
#         print(five.format("/ \\"))
#         print(six)
#
# draw_man(0)
# draw_man(1)
# draw_man(2)
# draw_man(3)
# draw_man(4)
#
# # active = True
# #
# # while active:
# #
# #     os.system("clear")
# #     current_word =input("Enter a word between 3 and 10 characters:\n> ").upper()
# #
# # listed_word = list(current_word)
# #
# # blanks = "_" * len(listed_word)
# # blanks_list = list(blanks)
# # attempts = 4
# # rounds = 0
# #
# # os.system("clear")
# # draw_man(rounds)
# # print(" ")
# # print("You have {} lives left.".format(attempts))
# # print(" ".join(blanks_list))
# #
# # while attempts > 0:
# #
# #     if listed_word != blanks_list:
# #
# #     guess = input("Take a guess:\n> ")
# #     guess = guess.upper()
# #
# #     if guess in listed_word:
# #         for x in range(0, len(listed_word)):
# #             if guess.upper() == listed_word[x]:
# #                 blanks_list[x] = guess
# #             else:
# #                 print("Nope!")
# #                 rounds += 1
# #                 attempts -= 1
# #                 time.sleep(1)
# #
# #                 os.system("clear")
# #                 draw_man(rounds)
# #                 print(" ")
# #                 print("You have {} lives left.".format(attempts))
# #                 print(" ".join(blanks_list))
# #
# #     else:
# #         os.system("clear")
# #         draw_man(rounds)
# #         print(" ")
# #         print("")
# #         print(" ".join(blanks_list))
# #         print("You got it!")
# #         print("You guessed it in {} attempts.".format(10 - attempts))
# #
# #         play_again = input("Would you like to play again? (y/n) > ")
# #     if play_again.lower() == "y":
# #         active = True
# #     else:
# #         active = False
# #         break
# #
# #     else:
# #         os.system("clear")
# #         draw_man(rounds)
# #         print(" ")
# #         print("")
# #         print(" ".join(listed_word))
# #         print("GAME OVER. Out of guesses.")
# #         play_again = input("Would you like to play again? (y/n) > ")
# #     if play_again.lower() == "y":
# #         active = True
# #     else:
# #         active = False
# #
# #     else:
# #         os.system("clear")
# #         print("")
# #         print("Thanks for playing. Goodbye!")
