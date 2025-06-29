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
