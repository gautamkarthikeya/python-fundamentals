#Area of rectangle
def area_of_rectangle():
    side1=float(input('enter length of rectangle:')) 
    side2=float(input('enter breadth of rectangle:'))
    area=side1*side2
    print ('area of rectangle for length {} and breadth {} is {}'.format(side1,side2,area))


#area of square
def area_of_square():
    side=float(input('enter side length of square:'))
    area=side*side
    print ('area of square for side {} is{}'.format(side,area))

#Area of circle
def area_of_circle():
    pi=3.14
    radius=float(input('enter radius of circle:')) 
    area=pi*radius**2
    print ('area of circle for radius {} is {}'.format(radius,area))

#Area of triangle
def area_of_triangle():
    Base=float(input('enter base of triangle:')) 
    height=float(input('enter hight of triangle:'))
    area= (Base*height)/2
    print ('area of triangle for Base {} and height {} is {}'.format(Base,height,area))

#area of trapezium
def area_of_trapezium():
    Base=float(input('enter base of trapezium:')) 
    top=float(input('enter length of the top of trapezium:'))
    height=float(input('enter height of trapezium:'))
    area=(Base+top)*height
    print ('area of trapezium for base {}, top {} and height {} is{}'.format(Base,top,height,area))


#area of paralellogram
def area_of_paralellogram():
    Base=float(input('enter base of paralellogram:')) 
    height=float(input('enter height of parellogram:'))
    area=Base*height
    print ('area of paralellogram for Base {} and height {} is {}'.format(Base,height,area))

