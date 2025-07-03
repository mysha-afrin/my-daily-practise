def test(a, b):
    '''a simple function that prints 2 parametes'''
    print(a)
    print(b)
test(1, 2)
print(test.__doc__)
help(test) #

print("Hey there")


#If i want return value in function then should use return.
def test(a:int = 10, b:int = 0) -> int : #This action indicates we are expecting our values to be integers.
    print(a)
    print(b)
    return a + b
test(1, 2)
print(test.__doc__)
help(test)
