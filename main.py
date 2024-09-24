import os, time
title = "Rainbow-ising Sentence Application"

os.system("clear")
print(f"{title: ^60}")
print()
sentence = input("What sentence do you want rainbow-ising? ")

for letters in sentence:
  if letters.lower() == "r":
    print("\033[91m", end="")
  elif letters.lower() == "y":
    print("\033[93m", end="")
  elif letters.lower() == "b":
    print("\033[96m", end="")
  elif letters.lower() == "g":
    print("\033[92m", end="")
  elif letters == " ":
    print("\033[0m", end="")
  print(letters, end="")


  
