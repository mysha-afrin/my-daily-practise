while True:
    print("Infinite loop")
    break
#Without the break this code will run forever.
x = 0
while x < 10:
    x +=1
    print(x)
    
    if x == 5:
        print("x is 5.")




my_list = []
counter = 0
while counter <= 100:
    if counter %2 == 0:
        if counter != 0:
            my_list.append(counter)
    counter += 1
print(my_list)
