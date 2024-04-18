print("Hello World")
x = 8
print(x)



if x == 7:
    print("yes")
if x != 7:
    print("no")



nums = [10, 20, 30, 40, 50]
for i in range(len(nums)):
    print(nums[i])

for val in nums:
    val += 5
    print(val)
print(nums)

for i, val in enumerate(nums):
    print("i is", i, "and val is", val)




dogs = ["boomer", "rocky", "daisy"]
for i in range(len(dogs)):
    print(dogs[i])

for name in dogs:
    print(name)
print(dogs)

for i, name in enumerate(dogs):
    print("i is", i, "and name is", name)



numbers = [1, 2, 3, 4, 5]
sum = 0
for val in numbers:
    sum += val
print(f"the sum is {sum}")



def hello(name = "John"):
    print("Hello!", name)
hello("Owen")
hello()



fname = 'Owen'
lname = "Gardner"

print(fname)
print(lname)
print("She's a great dancer")
print('He said "Hi" to his friend')

full_name = fname + " " + lname
print(full_name)
print(fname * 3)



platform_computing = "platform computing"
platform = platform_computing[:8]
print(platform)
computing = platform_computing[9:]
print(computing)



nums = [0, 3, 8, 5, 4]
tmp = nums[2]
nums[2] = nums[4]
nums[4] = tmp
print(nums)