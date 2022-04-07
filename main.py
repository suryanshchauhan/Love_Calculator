# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
initial = name1 + name2
lower = initial.lower()
true_total = lower.count("t") + lower.count("r") + lower.count("u") + lower.count("e")
love_total = lower.count("l") + lower.count("o") + lower.count("v") + lower.count("e")
true_love = str(true_total)+str(love_total)
print(type(true_love))
love_score = int(true_love)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  
  