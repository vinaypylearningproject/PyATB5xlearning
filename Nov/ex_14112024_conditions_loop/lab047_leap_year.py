year=int(input("enter the number here: "))


'''if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''

if year%400==0 and year%100==0:
    print("{0}  is leap year".format(year))
elif year%4==0 and year%100!=0:
    print("{0} is leap year".format(year))
else:
    print("{0} is not leap year".format(year))