print ('Enter 2 numbers to calculate LCM')
num1=int(input('Enter your first number'))
num2=int(input('Enter your second number'))

for G in range (2,(num1 *num2)+1,1):
    #print(G%num1,G%num2)
    if (G%num1 ==0) and (G%num2==0):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        print ('Lcm of these numbers are',G)
        break
    
