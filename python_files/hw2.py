# Hunter Porro
# Cite any sources you used to help with the homework 
'''
Implementing a Set: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
Dubugging: Google Gemini
Worked on 2 methods with Megan Weaver
'''

# including TAs and classmates
#to replace first and last I divided it up into 3 parts beginning middle and last got the string for each section then combined them
def exchange(str):
    """
    Given a string, return a new string where the first and last chars
    have been exchanged.
    """
    if len(str) <= 1:
        return str
    firstLetter = str[0]
    lastLetter = str[len(str)-1]
    middleLetters = str[1:-1]
    return lastLetter + middleLetters + firstLetter

#test
#string = "hello"
#print(exchange(string))

#For this method I used a compression statment that looks at each value in list and sees if it is not the range 5-7, if not it returns it as an updated list
def remove_range(alist, min, max):
    """
    Use a list comprehension to write a method named removeRange that accepts a list of
    integers and two integer values min and max as parameters and removes all elements
    values in the range min through max (inclusive).
    For example, if a list named alist stores
    [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], the call of remove_range(alist, 5, 7);
    should change the list to store [9, 4, 2, 3, 1, 8].

   *** Important: your code must use comprehensions and should not be more than
   two lines of code including the return statement ***
    """
    return [i for i in alist if i < min or i > max]
# #test
# testList = [7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7]
# print(remove_range(testList,5,7))

''' 
Similar to unique() in java set allows you to get only the unique values of strings in each 
Once updating them into a new list I took length of that list to get number of strings in the list 
'''
def word_count_in_set(words):
    """
    Write a function named wordCount that accepts a list of strings as a parameter and
    returns a count of the number of unique words in the list. Do not worry about
    capitalization and punctuation; for example, "Hello" and "hello" and "hello!!" are
    different words for this problem.
    *** Solution should not be more than 3 lines of code (can be less)
     including the return statement ***
    """
    uniqueWords = set(words)
    return len(uniqueWords)

#test
#words1 = ["Hello", "world", "hello", "Hello"]  
#print(word_count_in_set(words1))

'''
This function looks for where ice cream is in the dictionary and if it is then 
it replaces all instances with cheery - then for all cases bread values with butter 
'''
def topping1(dictionary):
    """
    Given a dictionary of food keys and topping values, modify and return the dictionary
    as follows:
    if the key "ice cream" is present, set its value to "cherry".
    In all cases, set the key "bread" to have the value "butter".
    Examples:
    topping1({"ice cream": "peanuts"}) returns {"bread": "butter", "ice cream": "cherry"}
    topping1({})  {"bread": "butter"} returns {"bread": "butter"}
    topping1({"pancake": "syrup"}) returns {"bread": "butter", "pancake": "syrup"}
    """
    if "ice cream" in dictionary:
        dictionary["ice cream"] = "cherry"
    dictionary["bread"] = "butter"
    return dictionary


#I created unique words list and put it into the comprehension to change what the "word" for the count was

def word_count(strings):
    """
    The classic word-count algorithm: given an array of strings, return a dictionary with
    a key for each different string, with the value the number of times that string appears in the
    list.
    Examples:
    word_count(["a", "b", "a", "c", "b"]) returns {"a": 2, "b": 2, "c": 1}
    word_count(["c", "b", "a"]) returns {"a": 1, "b": 1, "c": 1}
    word_count(["c", "c", "c", "c"]) returns {"c": 4}
    *** Important: your code must use comprehensions and should not be more than two
    lines of code including the return statement ***
    """
    uniqueWords = set(strings)
    return {word: strings.count(word) for word in uniqueWords}


# used a dictionary for loop to see append friends bidirectionally
def friend_list(friend_dictionary):
    """
    Write a method named friendList that accepts a dictionary as a parameter and reads
    friend relationships and stores them into a new dictionary that is returned.
    You should create a new dictionary where each key is a person's name from the original
    simple dictionary, and the value associated with that key is a list of all friends of
    that person. Friendships are bi-directional:
    if Marty is friends with Danielle, Danielle is friends with Marty.

    The dictionary parameter contains one friend relationship per key/value pair,
    consisting of two names. If the dictionary parameter,friendMap looks like this:
    Marty: Cynthia
    Danielle: Marty
    Then the call of friendList(friendMap) should return a dictionary with the following
    contents:
    {Cynthia:[Marty], Danielle:[Marty], Marty:[Cynthia, Danielle]}
    """
    friends = {}
    for name1, name2 in friend_dictionary.items():
        if name2 not in friends:
            friends[name2] = []
        if name1 not in friends:
            friends[name1] = []
        friends[name2].append(name1)
        friends[name1].append(name2)
    return friends


# Test functions
assert exchange("code") == "eodc", 'exchange("code") expected eodc'
print("correct")
assert exchange("ba") == 'ab', 'exchange("ba") expected ab'
print("correct")
assert exchange("a") == 'a', 'exchange("a") expected a'
print("correct")

assert remove_range([7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], 5, 7) == [9, 4, 2, 3, 1, 8] , '[9, 4, 2, 3, 1, 8] expected'
print("correct")
assert remove_range([7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], 2, 3) == [7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], '[7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7] expected'
print("correct")
assert remove_range([7, 9, 7], 7, 9) == [], '[] expected'
print("correct")

assert word_count_in_set(["the", "quick", "brown", "fox", "brown"]) == 4, 'expected 4'
print("correct")
assert word_count_in_set(["brown", "brown"]) == 1, 'expected 1'
print("correct")

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}, 'expected {"bread": "butter", "ice cream": "cherry"}'
print("correct")
assert topping1({"bread": "butter"}) == {"bread": "butter"}, 'expected {"bread": "butter"}'
print("correct")
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}, '{"bread": "butter", "pancake": "syrup"}'
print("correct")

assert word_count(["a", "b", "a", "c", "b"]) == {"a": 2, "b": 2, "c": 1}, 'expected {"a": 2, "b": 2, "c": 1}'
print("correct")
assert word_count(["c", "b", "a"]) == {"a": 1, "b": 1, "c": 1}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")
assert word_count(["c", "c", "c", "c"]) == {"c": 4}, 'expected {"a": 1, "b": 1, "c": 1}'
print("correct")

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")


# Problems found on https://codingbat.com/python