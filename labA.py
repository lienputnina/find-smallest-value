# Liene Putniņa, lr12022
# A4. Given n integers. Calculate the minimum value of given integers and the number of the integers with this value.
# Program created at: 2021/03/01

#VALIDATION
#ADD TO TEST PLAN

def findNumbers ():
    
    numbers = [];
    listNum = int(input("Enter the number of elements in a list: \n"))

    for i in range(1, listNum + 1):
        ele = int(input(f"Enter {listNum} numbers: "))
        numbers.append(ele)
        # ele = x;

    result = 0;
    for ele in numbers:
        if(ele == x):
            result = result + 1

# def countX(lst, x): 
#     count = 0
#     for ele in lst: 
#         if (ele == x): 
#             count = count + 1
#     return count 
  
# # Driver Code 
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
# x = 8
# print('{} has occurred {} times'.format(x, countX(lst, x))) 

    print("The smallest number is:", min(numbers) + "It occurs {result} times")

    
print(findNumbers())

repeatExec = True;

while repeatExec:
    count = input ("Enter 1 to continue or 0 to quit \n")
    print(findNumbers())
    if(count == "0"):
        repeatExec = False;
        break



