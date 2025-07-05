my_list = []
for num in range(0, 100):
    my_list.append(num)
    print(my_list)

#The block of code upper and lower works the same.

my_list_comprehension = [num for num in range(0, 100)]
print(my_list_comprehension)
