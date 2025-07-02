a = 10
'''This is example of scope .The a above and in function have no connection.They are completely seperate.'''
def test_func():
    print(a)
test_func()


a = 3
def test_func_3():
    print(a)
test_func_3()
