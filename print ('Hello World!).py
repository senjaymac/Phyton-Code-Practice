
print ('Hello World!')

b = "Senon"
print(b[1:5])
length = len(b)
print(length)
"""

input_string = "Hello"

reversed_string = ""

for char in input_string[::-1]:
   reversed_string += char

   print("The reversed string is:", reversed_string)
"""
"""
# Python code: Find the Maximum Number in a List

# Initialize the list of numbers
numbers = [3, 7, 2, 8, 5, 10, 6]

# Initialize the max_number to the first element in the list
max_number = numbers[0]

# Iterate through each number in the list starting from the second element
for number in numbers[1:]:
    # Check if the current number is greater than max_number
    if number > max_number:
        # Update max_number to the current number
        max_number = number

# Output the result
print("The maximum number in the list is:", max_number)

"""
import math
"""
n = 29

if n < 2:
    print(f"{n} is not a prime")

else:
    is_prime = True

    for i in range(2, int(math.sqrt(n)) + 1):
        # Check if n is divisible by i
        if n % i == 0:
            is_prime = False
            break
    
    # Output the result based on whether divisors were found
    if is_prime:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
"""
"""
Num = 5
factorial = 1

if Num < 0 :
    print("factorial is not defined for negative numbers")
else:
    for i in range (1, Num + 1):
        factorial *= i

        print (f"the factorial {Num} is:", factorial)

"""
"""
# python program : list of even perfect square

def find_even_perfect_squares(limit):
    even_perfect_squares = []
    i = 1

    while True:
        square = i * i
        if square >= limit:
            break
        if square % 2 == 0:
            even_perfect_squares.append(square)
        i += 1
    return even_perfect_squares


# asks the user for a number (n). 
try:
    n = int(input("Input a number "))
    if  n <=0:
        print("please enter a positive integere.")
    else:
        # find the list of even perfect squares
        even_squares = find_even_perfect_squares(n)
        print(f"Even perfect squares less than {n}: {even_squares}")
except ValueError:
    print("invalid Input")

    """
"""
def two_sum(nums, target):
    # Create a dictionary to store numbers and their indices
    num_map = {}
    
    # Loop through the list
    for i, num in enumerate(nums):
        # Calculate the complement that we need to find
        complement = target - num
        
        # If the complement exists in the dictionary, return the indices
        if complement in num_map:
            return [num_map[complement], i]
        
        # Otherwise, add the current number and its index to the dictionary
        num_map[num] = i

# Example usage:
nums = [6, 2, 4, 4]
target = 8
print(two_sum(nums, target))  # Output: [0, 1]


thislist = ["0apple", "1banana", "2cherry"]
thislist.append("3orange")

thislist.insert(4, "Watermelon")

Tropical = {"0Mango, 1Pineapple, 3Papaya"}
thislist.extend(Tropical)
print(thislist)

thislist2 = ["apple", "banana", "cherry"] #contents in the lists are mutable/changeable
thistuple = ("kiwi", "orange") #this is a tuple and contents in this tuple are immutable
thislist2.extend(thistuple)
print(thislist2)

del thislist[0] # delete 0Apple from the list
print(thislist) 

"""
"""
#get product of 2 numbers without using multiplication

def multiply(n, m):
    result = 0
    for _ in range(abs(m)):
        result += n

        if m < 0:
            result = -result
    return result
n = 3
m = 2
print(multiply(n , m))  

"""

#strings 
first_name = "Joe"
food = "pizza"
Email = "joe@fake.com"

print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"Your email is: {Email}")
print(f"{first_name} is {age} and his favorite food is {food} you can contact him thru his email account: {Email}")


#integeres
age = 25
quantity = 3

#float
GPA = 2.21
Price = 19.50
Distance = 10


#Boolean