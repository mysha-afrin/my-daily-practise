#list unpacking.
def print_all(first, *arguments):
    #Print all argument.
    for argument in arguments:
        print(argument)
print_all(1, 2, 3, 4, 'hello')



#keyword unpacking.
def print_more(**arguments):
    print(arguments)
    #print all(1, 2, 3, 4, 'hello')
print_more(arg1 = '1', arg2 = 'test', arg3 = [1, 2, 3])
