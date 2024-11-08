import pandas as pd
import sys
import time

a = 0
b = 0

# Ask the Question
print("Question 1: Do you like romance or horror movies?")
print("a) Romance")
print("b) Horror")

while True:
  answer = input("Your answer: ")
  if answer == 'a':
    a += 2
    break
  elif answer == 'b':
    b += 2

print("\n")

film_rec = ""

if a > b:
    # movie = emma (in excel)
    film_rec += id.read_excel(r"E:/Desktop/MOVIES_ONE.xlsx", sheetname = "'Sheet1")
else:
    # movie = IT (in excel)
    film_rec += id.read_excel(r"E:/Desktop/MOVIES_ONE.xlsx", sheetname = "'Sheet2")

print(f"\nTonight, you should watch:\n{film_rec}")
