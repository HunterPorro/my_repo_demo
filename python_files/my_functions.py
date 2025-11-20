# Hunter Porro
# Cite any sources you used to help with the homework including TAs and classmates
'''
Intro Slide Decks
https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
Python library on Python string method - https://docs.python.org/3/library/stdtypes.html
Google Gemini for debugging 
'''

'''
Assignment
In my_functions.py, create two python functions  the first function should take a list as an input parameter and return an integer. 
The second function can include any number of input parameters and return whatever youd like. The functions can do whatever
youd like them to do. The purpose is to write a complete python script which calls
functions. Include comments that describe what each function does inside the function
using “”” for comments. 
6. Create three calls to each function with test data to test them out. You do not need to use assert statements
'''


#function 1
def returnAvgInt (input):
    '''
    take a list as an input parameter and return an integer 
    for this function I created an average function that averages the inputed list 
    it then converts output from float to int
    '''
    averageInt = int(sum(input)/len(input))
    return averageInt

#function 2
applicants = {}

def collegeAcceptance(student,sat,essayScore,extracurriculars, teacherRec):
    """
    This function determines if a student is accepted to the college based on their scores and creates a dictionary of acceptance results    
    Parameters:
    student: The name of the student
    sat: The student's SAT score
    essayScore: The student's essay score (out of 100)
    extracurriculars: A score representing extracurricular involvement (out of 100)
    teacherRec: A score representing the teacher recommendation (out of 100)
    """
    if(sat>1400 and essayScore > 90 and extracurriculars > 90 and teacherRec >90):
        applicants[student] = "Accepted"
    else:
        applicants[student] = "Reject"        

#6. 3 calls to each function with test data

#function 1
print('function 1')
list1 =[1,234,435,546,67,343]
list2 = [34,234,212,12,12,33]
list3 = [22,21,1232,1382,192,7]
print(returnAvgInt(list1))
print(returnAvgInt(list2))
print(returnAvgInt(list1))
#function 2
print()
print('Function 2')
collegeAcceptance("Ryan", 1450, 95, 92, 98)
collegeAcceptance("Hunter", 1350, 95, 92, 98)
collegeAcceptance("Patrick", 1500, 91, 92, 98)

print(applicants)