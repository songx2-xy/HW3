year=input("Please input a year: ")
if year.isdigit():
    if (len(year)<=4):
        y=int(year)
        if (y%4==0):
            if(y%100==0):
                if(y%400==0):
                    print(y," is a leap year")
                else:
                    print(y," is not a leap year")
            else:
                print(y," is a leap year")
        else:
            print(y," is not a leap year")
    else:
        print("Error! Please input a year")
else:
    print("Error! Please input a number")