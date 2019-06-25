import os
import random

n = 1000
nums = []
for i in range(n):
	nums.append(random.randint(-128, 127))

file = open("./array.h", 'w+')

file.write("#ifndef INCLUDE_ARRAY_H\n")
file.write("#define INCLUDE_ARRAY_H\n")

# build array not sorted
file.write("static int arr1[] = {\n")
for num in nums:
	s = str(num) + ","
	file.write(s)
file.seek(-1,1)
file.write("};\n\n")

# build sorted array
nums.sort()
file.write("static int arr2[] = {\n")
for num in nums:
	s = str(num) + ","
	file.write(s)
file.seek(-1,1)
file.write("};\n\n")

# define size
declare = "#define ARRAY_SIZE %d\n\n"%n
file.write(declare)

file.write("#endif")
file.close()
