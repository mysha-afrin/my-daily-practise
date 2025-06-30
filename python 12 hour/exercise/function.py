#make a function that have three parametres ,the last one is an operator.
def better_calculator(num1, num2, operator):
    if operator == 'plus':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == 'minus':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
better_calculator(2, 4, 'plus' )
better_calculator(6, 8, 'minus')


def test_function(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
test_function(1, arg2 = 2, arg3 = 34, arg4 = [2, 3, 4])#Positional argument can not come first.


#Create a function with three parametres ; person ,name ,weekdays
#Person and great should have a default argument'
def greater_function(person = 'jeba', great ='Hello', weekday = 'Sunday'):
    print(f"{great} {person} ")
    print(f"Today is {weekday}")
greater_function('Jeba', 'greer', 'Monday')
