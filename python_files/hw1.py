# Hunter Porro
# Cite any sources you used to help with the homework including TAs and classmates
'''
Intro Slide Decks
https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
Python library on Python string method - https://docs.python.org/3/library/stdtypes.html
Google Gemini for debugging in trimmed_string
'''


### this code splices the last 4 characters of the string input then makes 2 copies via *2
def last_4_doubled(string):
    """
    Given a string, return a new string made of 2 copies of the last 4 characters of the original string.
    The string length will be at least 4.
    """
    # Your code here
    last_four_characters=string[-4:]
    output=last_four_characters*2
    return output

#This use a for loop to iterate through the list - I stopped 2 short as the function is designed to look at the next 3 to see if is the sequence 789 
#returns true if sequence appearss
def has_789(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    7, 8, 9 appears in the list somewhere. 7, 8, 9 must occur in order.
    """
    # Your code here
    for i in range (len(nums)-2):
        if(nums[i]==7 and nums[i+1]==8 and nums[i+2]==9):
            return True
    return False 

#Created a counter that started at 0 that added one if i is x and 2+ was o (similar logic to last function) it then returned answer
def count_x_o(string):
    """
    Return the number of times that the string "x-o" appears anywhere in the given string,
    except we'll accept any character for the '-', so "xao", "xbo", etc. count.
    """
    # Your code here
    counterXo = 0
    for i in range (len(string)-1):
        if(string[i]=='x' and string[i+2]=='o'):
            counterXo+=1
    return counterXo
#test - used during testing of code
#string ="xbo xzo zsd f x-o"     
#print(count_x_o(string))


#count is used to see how often something appears in a given string - used a conditional statement to retrn true or false if count of both was the same
def samesunmoon(string):
    """
    Return True if the string "sun" and "moon" appear the same number of times in the given string.
    *** This can be simplified using a Python string method ***
    """
    # Your code here
    return string.count("sun") == string.count("moon")
#test - used to see if the code worked
# string ="sunmoonsunmoondf;lkskf"     
# print(samesunmoon(string))


#I first added all values together (sum/number of values = mean) and subtracted the min and max number
# I did this so that it would only subtract 1 min and 1 max value then subtracted 2 from the numscount
def trimmed_average(nums):
    """
    Return the "trimmed" average of a list of ints, which is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    # Your code here
    trimmed_sum = sum(nums) - min(nums) - max(nums)
    numsCount = len(nums) - 2
    return trimmed_sum // numsCount

#Test- used to test if function worked
# nums = [1,43,634,324,32,32]
# print(trimmed_average(nums))

# Test functions - Do not modify these.
assert last_4_doubled("HelloThere") == 'herehere', 'last_4_doubled("HelloThere") expected ereere'
print("Test 1 for last_4_doubled passed")
assert last_4_doubled("abcdefgh") == 'efghefgh', 'last_4_doubled("abcdefgh") expected efghefgh'
print("Test 2 for last_4_doubled passed")
assert last_4_doubled("ComputerScience") == 'enceence', 'last_4_doubled("ComputerScience") expected enceence'
print("Test 3 for last_4_doubled passed")
print("-" * 20)

assert has_789([7, 7, 8, 9, 7]) is True, '[7, 7, 8, 9, 7] has 789'
print("Test 1 for has_789 passed")
assert has_789([7, 7, 8, 1, 9]) is False, '[7, 7, 8, 1, 9] does not have 789'
print("Test 2 for has_789 passed")
assert has_789([7, 7, 8, 7, 8, 9]) is True, '[7, 7, 8, 7, 8, 9] has 789'
print("Test 3 for has_789 passed")
print("-" * 20)

assert count_x_o("x-ox_ox.o") == 3, 'x-ox_ox.o has 3'
print("Test 1 for count_x_o passed")
assert count_x_o("xxox.o") == 2, 'xxox.o has 2'
print("Test 2 for count_x_o passed")
assert count_x_o("xrooo") == 1, 'xrooo has 1'
print("Test 3 for count_x_o passed")
print("-" * 20)

assert samesunmoon("sunmoon") is True, 'sunmoon has same sun/moon count'
print("Test 1 for samesunmoon passed")
assert samesunmoon("sunlightmoon") is True, 'sunlightmoon has same sun/moon count'
print("Test 2 for samesunmoon passed")
assert samesunmoon("sunmoonmoon") is False, 'sunmoonmoon does not have same sun/moon count'
print("Test 3 for samesunmoon passed")
print("-" * 20)

assert trimmed_average([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("Test 1 for trimmed_average passed")
assert trimmed_average([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("Test 2 for trimmed_average passed")
assert trimmed_average([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("Test 3 for trimmed_average passed")
print("-" * 20)
print("All tests passed! Great job!")

