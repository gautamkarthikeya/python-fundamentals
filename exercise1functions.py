

def say_hello(name,lastname='Palakollu'):
    print('Hi {}!'.format(name))

def square_numbers(number):
    return number*number



name = input('Whats your name:')
say_hello(name,'Karthikeya')
squared_number = square_numbers(7)
print('Square number for 7 is {}'.format(squared_number))

