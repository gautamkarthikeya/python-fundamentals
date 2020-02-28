Kilometres=float(input('Enter the amount of kilometeres you want to convert to miles:'))
fahrenhiet=round(Kilometres/1.609,2)
print(Kilometres, "kilometres are ",fahrenhiet, "miles")

miles=float(input('Enter the amount of miles you want to convert to kilometres:'))
kilometres=round(miles*1.609,2)
print(miles, "miles are ",kilometres, "kilometres")




celcius=float(input('Enter the amount of degrees celcius you want to convert to degrees fahrenhiet:'))
fahrenhiet=round((celcius*9/5)+32,2)
print(celcius, "degrees celcius are ",fahrenhiet, "fahrenheit")

fahrenhiet=float(input('Enter the amount of fahrenhiet you want to convert to degrees celcius:'))
celcius=round((fahrenhiet-32)*5/9,2)
print(fahrenhiet, "fahrenhiet celcius are ",celcius, "celcius")




year=int(input('Enter a year you want to know is a leap year'))

if (year%4==0 or year%400==0) and year%100!=0:
    print(year,' is a leap year')
else:
    print(year,' is not a leap year')

# if year%4==00:
#     if year%100==0:
#         if year%400==0:
#             print(year,' is a leap year')
#         else:
#             print(year,' is not a leap year')
#     else:        
#         print(year,'is not a leap year')















































































