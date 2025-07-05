my_list = []
for num in range(0, 100):
    my_list.append(num)
    print(my_list)

#The block of code upper and lower works the same.

my_list_comprehension = [num for num in range(0, 100)]
print(my_list_comprehension)



#Combine a list comprehension.
my_list = [num for num in range(0, 100) if num< 10] #Here in this condition else don't work.
print(my_list)
my_list1 = [num if num < 10 else 0 for num in range(0, 100)] #This line is more powerful than the upper one.
print(my_list1)


combined_comb = [x for x in range(5)]
print(combined_comb)

combined_comb = [[x for x in range(5)] for y in range(10)]
for row in combined_comb:#This statement here shows the list in row.
    print(row)
