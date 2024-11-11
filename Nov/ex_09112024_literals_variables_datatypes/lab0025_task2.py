# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

#Division method(//)
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
Q=num1//num2
print("quotient is: ",Q)
R=num1%num2
print("reminder is :",R)

#divmod() function

Q,R=divmod(15,2)
print("quotient is: ",Q)
print("reminder is :",R)


