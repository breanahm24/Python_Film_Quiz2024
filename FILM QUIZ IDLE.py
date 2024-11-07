# importing sys to read functions and vairables,
# time to read time related functions
import sys
import time

# set question scores to 0
a = 0
b = 0
c = 0
d = 0

# introduction typing effect
def typing(t):
  for char in t:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

typing("Welcome to the What to Watch Quiz!\n")
time.sleep(1)
typing("This quiz will help you decide what to watch using your mood and preferences!\n") 
time.sleep(.5)
typing("To answer, please type your answer in lowercase and press enter.\n")
print("\n")

# start printing the questions, the code for each question: rinse and repeat
time.sleep(1)
# Question 1
print("Question 1: How are you feeling today?")
print("a) Happy and Energised")
print("b) Calm and Content")
print("c) Romantic")
print("d) Sad and Somber")

# adding sums to the original set code where each variable was '0'
while True:
  answer = input("Your answer: ")
  if answer == 'a':
    a += 2
    break
  elif answer == 'b':
    b += 2
    break  
  elif answer == 'c':
    c += 2
    break
  elif answer == 'd':
    d += 2
    break
  else:
    print(input("Try again: "))
    break

print("\n")
# Question 2
print("Question 2: What is your ideal genre for today?")
print("a) Action")
print("b) Drama")
print("c) Romantic")
print("d) Horror")

while True:
  answer = input("Your answer: ")
  if answer == 'a':
    a += 2
    break
  elif answer == 'b':
    b += 2
    break  
  elif answer == 'c':
    c += 2
    break
  elif answer == 'd':
    d += 2
    break
  else:
    print(input("Try again: "))
    break

print("\n")
# Question 3
print("Question 3: What ending are you hoping for?")
print("a) Uplifting and aspirational")
print("b) Sad yet beautiful")
print("c) Fulfilled heart")
print("d) Sudden twist")

while True:
  answer = input("Your answer: ")
  if answer == 'a':
    a += 2
    break
  elif answer == 'b':
    b += 2
    break  
  elif answer == 'c':
    c += 2
    break
  elif answer == 'd':
    d += 2
    break
  else:
    print(input("Try again: "))
    break

print("\n")
# Question 4
print("Question 4: Do you want something light or deep?")
print("a) Light")
print("b) Deep")
print("c) Something in between")

while True:
  answer = input("Your answer: ")
  if answer == 'a':
    a += 2
    break
  elif answer == 'b':
    b += 2
    break  
  elif answer == 'c':
    c += 2
    break
  else:
    print(input("Try again: "))
    break
print("\n")

typing("Films loading, please wait...")
time.sleep(1)

# printing and discovering the quiz answers for the user using loop functions
film_rec = ""

if a > b:
  film_rec += "21 Jump Street (2012)\n"
else:
  film_rec += "Billy Elliot (2000)\n"

if a > c:
  film_rec += "10 Things I Hate About You (1999)\n"
else:
  film_rec += "The Cabin In The Woods (2011)\n"

if a > d:
  film_rec += "Drive (2011)\n"
else:
  film_rec += "Lost in Translation (2003)\n"
  
if c > b:
  film_rec += "Call Me By Your Name (2017)\n"
else:
  film_rec += "A Ghost Story (2017)\n"


if c > d:
  film_rec += "Mr & Mrs Smith (2005)\n"
else:
  film_rec += "The Notebook (2004)\n"

if d > b:
  film_rec += "Notting Hill (1999)\n"
else:
  film_rec += "Warm Bodies (2013)\n"

if d > a:
  film_rec += "Fight Club (1999)\n"
else:
  film_rec += "Brokeback Mountain (2005)\n"

if d > c:
  film_rec += "Romeo + Juliet (1996)\n"
else:
  film_rec += "The Lighthouse (2019)\n"

print(f"\nTonight, you should watch:\n{film_rec}")
