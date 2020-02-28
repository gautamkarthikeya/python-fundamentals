
number=(int(input('enter how many rows:')))
for num in range (number,1,-1):
   # all prime numbers are greater than 1
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num,end=",")
    

triangles=int(input('enter how many stairs are there in this pyramid'))
for row in range (1,triangles+1):
    for column in range (1,row+1):
        print(column,end="")
    print()

'''triangles=int(input('enter how many stairs are there in this pyramid'))
for row in range (1,triangles+1):
    for column in range (1,row+1):
        print(row,end="")'''

number=(int(input('enter how many rows:')))
for G in range (number,0,-1):
    for A in range (1,G+1,1):
        print(A, end = '')
    print()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
