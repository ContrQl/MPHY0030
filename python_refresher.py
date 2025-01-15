## navigating lists
list_final = [1, 2, 3, [4, 5]]
second_elem = list_final[1]
first_of_last_elem = list_final[-1][0]

print(len(list_final), len(list_final[-1]))

## integer and list slicing
print(list_final[0:3])

my_str = 'Hi my name is Mujie'
print(my_str[3:10])

my_str_1 = 'Hi my name is Shaheer'
my_str_2 = 'Hi my name is Name'

print(my_str_1[14:])
print(my_str_2[14:])

## function that returns true if any value appears twice in list, false if isdistinct
def iseverythingunique(numbers):
    flag = 'Yes'
    list_2 = []
    for number in numbers:
        if number in list_2:
            flag = 'No'
            break
        else:
            list_2.append(number)
    return flag

print(iseverythingunique([1,1,1,3,3,4,3,2,4,2]))

import os
print(os.listdir('./'))

from csv import writer
List = [6, 'William', 5532, 1, 'UAE']
with open('event.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close()

import datetime
current_date_time = datetime.datetime.now()
dt_string = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
print("date and time:", dt_string)

import time
tic = time.time()
my_list = []
for i in range(100000):
    my_list.append(42)
toc = time.time()
time_taken = toc-tic
print(f'It took {time_taken} seconds')

import sys
X = sys.argv[1]
print(f"Hello world! I am a script and I was given the number {X}")