practise_list = [[10, 40, 20, 50], [2, 42, 10], [101, 10, 4]]
#Use a for loop to only print numbers below 50.

for nested_list in practise_list:
    
    for list in nested_list:
        
        while True:
            if list < 50:
                print(list)
                break



#Skip values below 10.

practise_list = [[10, 40, 20, 50], [2, 42, 10], [101, 10, 4]]
for nested_list in practise_list:
    
    for list in nested_list:
        
        if list > 10:
            print(list)


#
