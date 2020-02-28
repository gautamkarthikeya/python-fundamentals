
while True:

    year_str=input('Enter a year you want to know is a leap year (to exit enter -1):')
    year = -1
    try:
        year = int(year_str)
    except:
        #start execution again if user enters invalid number by continue
        continue

    if year<=-1:
        break

    if (year%4==0 and year%100!=0) or year%400==0:
        print(year,' is a leap year')
    else:
        print(year,' is not a leap year')