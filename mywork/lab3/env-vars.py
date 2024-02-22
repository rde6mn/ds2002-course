#!/usr/local/bin/python3


import os

os.environ["FAV_COLOR"] = "Blue"
os.environ["BIRTH_MONTH"] = "March"
os.environ["FAV_SNACK"] = "Chips"


FAV_COLOR = input('What is your favorite color? ')
BIRTH_MONTH = input('What month were you born? ')
FAV_SNACKS = input('What is your favorite snack? ')


print(FAV_COLOR)
print(BIRTH_MONTH)
print(FAV_SNACKS)
