# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

def writeFileToList(file):
    nums = []
    with open(file, 'r') as of:
        line = of.readline()
        while line:
            line = line.strip()
            nums.append(int(line))
            line = of.readline()

    return nums

def compareList(a, b):
    return [item for item in a if item in b]


nums1 = writeFileToList('1.txt')
nums2 = writeFileToList('2.txt')

print(compareList(nums1, nums2))