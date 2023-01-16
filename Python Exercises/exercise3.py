#Exercise 3 - Odd and Even

# def isOdd(x):
#     if x % 2 == 1:
#         print(True)
#     else: 
#         print(False)
    
# def isEven(x):
#     if x % 2 == 0:
#         print(True)
#     else: 
#         print(False)

def isOdd(number):
    return number % 2 == 1

def isEven(number):
    return number % 2 == 0     


assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
