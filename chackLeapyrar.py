year = int(input("enter year to chack leap year  "))

if year % 100 == 0 :
    if year % 400 == 0 : 
        print(year, " is leap year  ")
    else :
        print(year, "  is not a leap year ")
    
    
elif year % 4 == 0 :
    print(year, "is leap yeaar")
else:
    print(year, "not a leap year")