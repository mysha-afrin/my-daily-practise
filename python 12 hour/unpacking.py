#list unpacking.
def print_all(first, *arguments):
    #Print all argument.
    for argument in arguments:
        print(argument)
print_all(1, 2, 3, 4, 'hello')
