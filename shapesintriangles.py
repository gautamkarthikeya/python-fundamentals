rows=int(input('Enter number of rows in the triangle'))
for number in range (1,rows+1):
    print (" "*(rows-number)+"* "*number)

list = [' **     **  ','*    *     *','*          *','  *      *  ','      *     ']

for i in range (0,8000):
    for j in range(1,rows+1):
        print(list[i],end="   ")
    print()

print     (' **     ** ')                                                                                     
print     ('*    *     *')                                                                        
print     ('*          *')                                                                        
print     ('  *      *  ')                                                               
print     ('      *     ')                                             