# Liene Putniņa, lr12022
# A4. Given n integers. Calculate the minimum value of given integers and the number of the integers with this value.
# Program created at: 2021/03/01

# A function with the instructions for the program is declared
def findNumbers():
    numbers = []
    # User enters the volume of a list by writing an integer and the input is validated
    continueEntering = True
    while continueEntering:
        try:
            listNums = int(input("Enter the number of elements in a list: \n"))
        except ValueError:
            print("Invalid input. Please, enter integer")
            continue
        else:
            continueEntering = False

    # A loop that:
    # 1. Goes through the list of numbers the user has entered and prints them all out.
    # 2. Finds the smallest number
    for i in range(1, int(listNums) + 1):
        #Input validation
        continueEntering = True
        while continueEntering:
            try:
                allNums = int(input(f"Enter {listNums} numbers: "))
            except ValueError:
                print("Invalid input. Please, enter integer")
                continue
            else:
                continueEntering = False
                numbers.append(allNums)


        x = min(numbers);

    # A loop that finds the number of times an integer occurs in the list.
    result = 0
    for ele in numbers:
        if ele == x:
            result = result + 1

    # The smallest number in a list and its occurrence is printed
    print(f"The smallest number is: {x} It occurs {result} times")


# Definition of the repeatable value - it will be checked at the end of each execution cycle
repeatExec = True

# Execution of the program
while repeatExec:
    print(findNumbers())
    #Input validation
    continueEntering = True
    while continueEntering:
        try:
            count = int(input("Enter 1 to continue or 0 to quit \n"))
            
        except ValueError:
            print("Invalid input. Please, enter integer")
            continue
        else:
            continueEntering = False
    if count == 0:
        repeatExec = False
        break
    else:
        repeatExec = True
