# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

"""
s1=int(input("enter the value of score\n"))
if s1>=90 and s1<=100:
    print("Grade is :","A")
elif s1>=80 and s1<=89:
    print("Grade is:","B")
elif s1 >= 70 and s1 <= 79:
    print("Grade is:", "C")
elif s1 >= 60 and s1 <= 69:
    print("Grade of D is:", "D")
elif s1 >= 100 and s1 <= -1:
    print("You are  Superman!!, you can't get a grade!! 0:-1)")
else:
    print("Grade  is:","F")"""

score = int(input("Enter your score\n"))

if score >= 90 and score <= 100:
    print("You grade is ", "A")
elif score >= 80 and score <= 89:
    print("You grade is ", "B")
elif score >= 70 and score <= 79:
    print("You grade is ", "C")
elif score >= 60 and score <= 69:
    print("You grade is ", "D")
elif score >= 100 and score <= -1:
    print("You are  Superman!!, you can't get a grade!! 0:)")
else:
    print("You grade is ", "F")


