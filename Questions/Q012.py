nums = []

while((num := int(input())) != 0):
    nums.append(num)

for num in nums[::-1]:
    print(num)
