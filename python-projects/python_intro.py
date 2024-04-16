#print("hello world")

print(0%3)
#variables
'''
x = 100
y = 10
res = x/y
print(res)
res2 = x//y
print(res2)
'''


#elif
'''
x = -1

if x < 0:
    print('the value of x is', x, 'and it is less than 0')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is 0')
'''


#loops
'''
counter = 0
while counter < 10:
    print(counter)
    counter += 1

nums = [10, 25, 35, 40, 55]
for i in range(5):
    print(nums[i], end=" ")

print()

for i in range(len(nums)):
    print(nums[i], end=" ")
print()

for i in range(2, len(nums)):
    print(nums[i], end=" ")
print()

for num in nums:
    print(num, end=" ")
print()

for i, val in enumerate(nums):
    print("i is", i, "and val is", val)

'''


#loops_practice
'''
dogs = ["boomer", "rocky", "daisy"]

for i in range(len(dogs)):
    print(dogs[i], end = " ")
print()

for name in dogs:
    print(name, end = " ")
print()

for i, name in enumerate(dogs):
    print(name, end = " ")
print()


nums = [3214, 2341, 2315, 352]
sum = 0
for num in nums:
    sum += num
print(sum)
print(f"The sum is {sum}")
'''

#functions
'''
def hello(name):
    print("hi", name)

hello("barbie")
'''


#Strings
'''
f_name = "rebecca"
l_name = "jackson"

full_name = f_name +" "+ l_name
initial = f_name[0]
last = full_name[-1]
print(l_name[-2:])
'''

swap = [0, 3, 8, 5, 4]
temp = swap[2]
swap[2] = swap[4]
swap[4] = temp