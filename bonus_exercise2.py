import math
values=input('Enter a list of numbers separated by commas')

list = values.split(',')
results=[]
for number in list:
    D=float(number)
    H=30
    C=50
    result=math.sqrt ((2 * C * D)/H)
    results.append( str(round(float(result),3)))
print(','.join(results))