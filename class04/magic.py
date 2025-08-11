# recursion
# def print_to_given_number(n):
#     if n < 1:
#         return
#     print_to_given_number(n - 1)
#     print(n)
    
# print_to_given_number(10)


# traditional loop
# numbers = []
# for i in range(1, 1001):
#     numbers.append(i)
# print(numbers)


# List comprehension
numbers_by_list_comprehension = [i for i in range(1, 1001)]
# print("Numbers from 1 to 1000 using list comprehension:", numbers_by_list_comprehension)


# traditional if  else 
nums =  [i for i  in range(1,11)]
odd = []
for num in nums:
    if num % 2 == 0:
        continue
    else:
        odd.append(num)
# print("Odd numbers are:", odd)

# List comprehension with if condition
odd_numbers = [num for num in nums if num % 2 != 0]
print("Odd numbers using list comprehension:", odd_numbers)

# shorthand  if else 
switch = "on"
light = "light is On " if switch == "on" else "Light is Off"
# print(light)

# Multiple variables assignment
a, b, c = 1, 2, 3
# print("Multiple variables assignment:", a, b, c)
a, b, c = [4, 5, 6]
print("Multiple variables assignment from list:", a, b, c)