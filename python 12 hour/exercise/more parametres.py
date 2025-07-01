#exercise
#create a calculator function that prints the sum of an unlimited amount of numbers
def calculator_function(*argument):
    result = sum(argument)
    print(result)
calculator_function(1, 2, 3, 4, 5, 6)
