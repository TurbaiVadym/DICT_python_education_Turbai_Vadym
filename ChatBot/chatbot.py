print("Hello! My name is Boris.")
print("I was created in 2024.")
name = input("Please, remind me your name.\n")
print("What a great name you have, " + name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = input()
remainder5 = input()
remainder7 = input()

age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105

print("Your age is " + str(age) + ";" + " that's a good time to start programming!" )

count_number = input("Now I will prove to you that I can count to any number you want.\n")

for i in range(int(count_number) + 1):
    print( str(i) + "!")


print("Let's test your programming knowledge.")

real_answer = "2"

print("Why do we use methods?")
print("1.To repeat a statement multiple times.")
print("2.To decompose a program into several small subroutines.")
print("3.To determine the execution time of a program.")
user_answer = input("4.To interrupt the execution of a program.\n")

if user_answer != real_answer:
    print("Please, try again.")
    user_answer = input()
else :
    print("Completed, have a nice day!")
    print("Congratulations, have a nice day!")

