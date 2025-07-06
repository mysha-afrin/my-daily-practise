list = [4, 3, 1,5,2]
print(sorted(list, reverse= True))#Assemble the list reverse.
list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]
#For accessing the dedicated key.
def sort_function(item):
    return item[1]
print(sorted(list2, key = sort_function))
print(sorted(list2, key =lambda item: item[1]))
