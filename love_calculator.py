# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_d1 = 0
count_d2 = 0
name1 = name1.lower()
name2 = name2.lower()

count_d1 += name1.count("t")
count_d1 += name1.count("r")
count_d1 += name1.count("u")
count_d1 += name1.count("e")
count_d1 += name2.count("t")
count_d1 += name2.count("r")
count_d1 += name2.count("u")
count_d1 += name2.count("e")

count_d2 += name1.count("l")
count_d2 += name1.count("o")
count_d2 += name1.count("v")
count_d2 += name1.count("e")
count_d2 += name2.count("l")
count_d2 += name2.count("o")
count_d2 += name2.count("v")
count_d2 += name2.count("e")

count_d1 = count_d1 * 10
result = count_d1 + count_d2
if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together")
else:
    print(f"Your score is {result}")
