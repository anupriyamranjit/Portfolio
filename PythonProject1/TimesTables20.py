from random import randint
import time
score = 0
averagetime = []
while 1>0:
    term1 = randint(1,20)
    term2 = randint(1,20)
    product = term1*term2
    print('{Firstterm} x {Secondterm}'.format(Firstterm = term1,Secondterm = term2))
    start= time.time()
    timetaken = 0
    userInput = int(input("Answer:"))
    end = time.time()
    if userInput == product:
        print("That is correct")
        score += 1
    elif userInput == 1234567:
        print(score)
        sum = 0
        for i in range(len(averagetime)):
            sum = sum + averagetime[i]
        average = sum/len(averagetime)
        print(average)
        break
    elif userInput != product:
        print("That is wrong")
        print("The answer is {product}".format(product = product))
    averagetime.append(end - start)
    print(score)

def print_times_x(x):
    for n in range(x):
        m = n+1
        for i in range(x):
            print("{int}|".format(int = m*(i+1),end=' ')
    return 0

print_times_x(3)
