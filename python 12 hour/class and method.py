def add(a, b):
    return a + b
class Test:
    def __init__(self, add_function):
        self.add_function = add_function
test = Test(add_function = add)
print(test.add_function(1, 2))
