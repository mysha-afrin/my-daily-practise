#Open a file manually.
file = open('some.txt')
print(list(file))
file.close()

#open and close automatically.
with open('some.txt') as file:
    print(type(file.read()))

#open and close automatically.
with open('some.txt') as file:
    print(file.read())


#open a file in write mode.
with open('test.txt', 'a') as file:
    file.write("XXXXXXXXZZZZ")
