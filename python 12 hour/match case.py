grade = int(input("Enter your grade : "))
match grade:
    case 1:
        print("This is 1st case.")
    case 2:
        print("This is 2nd case.")
    case 3:
        print("This is 3rd case.")
    case 4:
        print("This is 4th case")
    case 5:
        print("This is 5th case.")
    case _:
        print("404error occured.")
