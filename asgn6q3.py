import asgn6q2
import random

#asking user for number of problems 
while True:
    problems = int(input("How many problems would you like to attempt?:"))
    if problems>0:
        break
    else:
        print("Invalid number, try again.")

#asking user for width of digits
width = int(input("How wide do you want your digits to be?:"))
while width<5 or width>10:
    print("Invalid number, try again.")
    width = int(input("How wide do you want your digits to be?:"))

#asking user for string to be used, only single digits accepted
strng = input("What character would you like to use?:")
while len(strng)!=1:
    print("String too long, try again.")
    strng = input("What character would you like to use?:")

#formatting
print()
print("Here we go!")
print()

def rand_op():
    op = random.randint(0,1)
    count=""
    if op == 0:
        return count+"minus"
    elif op == 1:
        return count+"plus"



count=0
for i in range(problems):
    #printing out the question
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    print("What is ...")
    print()
    asgn6q2.print_number(num1,width,strng)
    print()
    op=""
    ran = rand_op()
    if ran=="plus":
        print(asgn6q2.plus(width,strng))
        op="+"
    elif ran=="minus":
        print(asgn6q2.minus(width,strng))
        op="-"
    print()
    asgn6q2.print_number(num2,width,strng)
    print()

    #answer and answer validation
    ans = int(input("="))
    tot = asgn6q2.check_answer(num1,num2,ans,op)
    if tot==True:
        print("Correct!")
        count+=1
    else:
        print("Sorry, that's not correct.")
    print()
print("You got",count, "out of",problems,"correct!")