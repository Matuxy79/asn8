#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

from a8q2 import fibonacci

#part A
print(fibonacci(0)) # Expected Output: 0
print(fibonacci(1)) # Expected Output: 1
print(fibonacci(5)) # Expected Output: 5
print(fibonacci(10)) # Expected Output: 55

from a8q2 import moosonacci

#part B
print(moosonacci(0)) # Output: 0
print(moosonacci(1)) # Output: 0
print(moosonacci(2)) # Output: 1
print(moosonacci(5)) # Output: 11
print(moosonacci(10)) # Output: 125

from a8q2 import substr

#part C
print(substr("Hello, world!", "l", "x"))  # output: "Hexxo, worxd!"
print(substr("Hello, world!", "o", "i"))  # output: "Helli, wirld!"
print(substr("Hello, world!", "z", "q"))  # output: "Hello, world!"
print(substr("Hello, world!", "or", "q"))  # output: "Hello, wqld!"
print(substr("Hello, world!", "o", "ee"))  # output: "Hellee, weerld!"