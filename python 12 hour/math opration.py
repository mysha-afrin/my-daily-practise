
math = 10 + 5
result = math / 2
print(result)

test = "a word".upper()
print(test)

user_name = "jeBA mYsha".title().strip()
print(user_name)

exercise_pet = "I like puppies"
exercise_pet1 = exercise_pet.replace("puppies", "kitties")
print(exercise_pet1)


exer_pets = "I like puppies, puppies, puppies, puppies"
exer_pets1 = exer_pets.replace("puppies", "kitten",2)
print(exer_pets1)

test_value = 'Hello' + '\tworld'
print(test_value)




#NOTE#
'''List and tuples can store different types of data.Both can contain any kind of data.Even a tuple can contain a 
tuple and a list can contain a list.'''
'''Tuples are immutable and lists are mutable.'''
'''list.append(value) works
tuple.append(value) fails.'''
tuples = (1, 2, 3, 3, True ,("h", "K"))
print(tuples)



list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list[-1::-3])

a, b = (1, 2)
print(a)
print(b)
c, d = [20, 'Hello']
print(c)
print(d)


default_value = ['b', 'g', 'h']
print(default_value[1:2])



#turning a string into a list/tuple

test_string = "this is a string."
print(test_string.split())


my_num = {1, 2, 3, 4, 5}
##NOTE##
'''This method add index to set.'''
my_num.add(6)
print(my_num)
##NOTE##
'''This method remove an index to set.'''
my_num.remove(2)
print(my_num)




print(my_num)
print(len(my_num)) #Prints the length of set.


my_num1 = {1, 2, 3, 4, 5, 6, 7}
my_num2 = {8, 9, 10}
print(my_num1.union(my_num2))
print(my_num1.intersection(my_num2))



'''                               Comparison operators                              '''
"""== is equal
   != is not equal
   <, <= smaller than ,smaller or equal than."""


