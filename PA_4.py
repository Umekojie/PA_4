""" Participation activity 4
Josephine Cattell
this program will create a list of 100 random numbers from 1-10 """
import random

list_of_numbers = []
for i in range (1,10):
    list_of_numbers.append(random.randint(1,10))
print(len(list_of_numbers))
print(sum(list_of_numbers))
print(sum(list_of_numbers)/len(list_of_numbers))
