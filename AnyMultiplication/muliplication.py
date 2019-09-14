import numpy as np
from random import randint
def CreateRow(n,s):
    list = []
    for i in range(s):
        list.append(n*(i+1))
    print(list)




def MultiplicationTable(n,s):
    Table = []
    for i in range(n):
        Table.append(CreateRow(i+1,s))


def AskingQuestion(n,s):
    term_one = randint(1,n)
    term_two = randint(1,s)
    product = term_one*term_two
    print("{FirstTerm} x {SecondTerm}".format(FirstTerm=term_one, SecondTerm=term_two))
    user_input =int(input("Answer: "))
    if user_input == product:
        print("You are correct")
    else:
        print("Your wrong")
    AskingQuestion(n,s)




def main():
    User_input_choice = input("Press T for table or Q for questions ")
    if User_input_choice == "T":
        Size_of_Table = int(input("Length of Table "))
        Depth_of_Table = int(input("Depth of Table "))
        MultiplicationTable(Depth_of_Table,Size_of_Table)
    elif User_input_choice == "Q":
        RangeOne = int(input("Range: "))
        RangeTwo = int(input("RangeTwo: "))
        AskingQuestion(RangeOne,RangeTwo)

if __name__ == "main":
    main()


