# Q1) num = [1,2,3,4,5,6,7]
# k = 3
# given a list, and rotate list k times
# op = [5,6,7,1,2,3,4]
# num = [1,2,3,4,5,6,7]
# k=int(input("enter K:"))
# n=len(num)
# for i in range(k):
#     l=num.pop()
#     num.insert(0,l)
# print(num)
# Q2) Input  =  [[1, 2, 3], [4, 9, 3], [0, 3, 10] ,[2,1,7]]

# sort the above list based on 2nd element in nested lists
# # Output =  [[2,1,7] , [1,2, 3], [0, 3, 10] , [4, 9, 3]]
# input  =  [[1, 2, 3], [4, 9, 3], [0, 3, 10] ,[2,1,7]]
# l=sorted(input,key=lambda x: x[1])
# print(l)
# Q3) str1 = "hyd387era24bad61"
	# Create a python function to Print count of digit, count of characters and return string without digit

	# output:
	# 	Count of digits: 7
	# 	Count of characters: 9
	# 	hyderabad
str1 = "hyd387era24bad61"
def analyze_string(str1):
    digit_count = 0
    char_count = 0
    result = ""

    for ch in str1:
        if ch.isdigit():
            digit_count += 1
        elif ch.isalpha():
            char_count += 1
            result += ch

    print("Count of digits:", digit_count)
    print("Count of characters:", char_count)
    return result
