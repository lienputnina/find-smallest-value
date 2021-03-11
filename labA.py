# Liene Putniņa, lr12022
# A4. Given n integers. Calculate the minimum value of given integers and the number of the integers with this value.
# Program created at: 2021/03/01

# VALIDATION

# A function with the instructions for the program is declared
def findNumbers():
    numbers = []
    # User enters the volume of a list by writing an integer.
    listNums = int(input("Enter the number of elements in a list: \n"))

    # A loop goes through the list of numbers the user has entered and prints them all out.
    for i in range(1, listNums + 1):
        allNums = int(input(f"Enter {listNums} numbers: "))
        numbers.append(allNums)

    # A loop that:
    # 1.Finds the smallest integer in the list and prints it out,
    # 2. Finds the number of times this integer occurs in the array and prints out their value.
    result = 0
    for ele in numbers:
        if ele == min(numbers):
            result = result + 1

    print("The smallest number is:", min(numbers), ("It occurs {result} times"))


# Definition of the repeatable value - it will be checked at the end of each execution cycle
repeatExec = True

# Execution of the program
while repeatExec:
    print(findNumbers())
    count = int(input("Enter 1 to continue or 0 to quit \n"))
    if count == 0:
        repeatExec = False
        break
    else:
        repeatExec = True
