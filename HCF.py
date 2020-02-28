def compute_HCF (a,b):
    if b==0:
        return a
    else:
            return compute_HCF (b,a%b)

num1=float(input('Enter your first number'))
num2=float(input('Enter your second number'))
print (compute_HCF(num1,num2))




n=int(input('how many numbers do you want' ))
first=0
second=1
for G in range (n):
    print(first)
    temp=first
    first=second
    second=temp+second
    
