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
