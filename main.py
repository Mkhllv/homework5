# Exercise №1
from random import randint

my_list = [randint(1, 200) for i in range(20)]
for i in my_list:
    if i > 100:
        print(i, end=' ')
print()
# Exercise №2

my_list = [randint(1, 200) for i in range(20)]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_results)

# Exercise №3
my_list = [randint(1, 10) for i in range(4)]
if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
else:
    my_list.append(0)
print(my_list)
