#Question1
age = 15

#Question2
height = 54.5

#Question3
complex_numb = 2-5j

#Question4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is ", area)

#Question5
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

#Question6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is: ", area)
print("The perimeter of the reactangle is: ", perimeter)

#Question7
r = float(input("Enter radius: "))
pi = 3.14
area = pi * r * r
c = 2 * pi * r
print("The area of the circle is: ", area)
print("The circumference of the cicle is: ", c)

#Question8
slope = 2
y_intercept = -2
x_intercept = 1

#Question9
m = (6 - 2) / (10 - 2)

#Question10
print(slope > m)

#Question11
delta = (36)**2 - 4 * 9 * 1
x_1 = (-6 - delta**0.5) / 2
x_2 = (-6 + delta**0.5) / 2

#QUestion12
print(len('python') > len('dragon'))

#QUestion13
print('on' in 'python' and 'on' in 'dragon')

#Question14
print('jargon' in 'I hope this course is not full of jargon.')

#QUestion15
print('on' not in 'python' and 'on' not in 'jargon')

#Question16
print("Length of the text 'python': ", len('python'))

print("Length of 'python' in float: ", float(len('python')))

print("Length of 'python' in string: ", str(len('python')))

#Question17
number = 4
number % 2 #if result = 0 ==> number is even

#Question18
print((7 // 3) == int(2.7))

#Question19
print(type('10') == type(10)) # False

#Question20
print(int(float('9.8')) == 10)

#Question21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is ", hours * rate)

#Question22
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for ", seconds, " seconds.")

#Question23
print(1, ' ', 1, ' ', 1, ' ', 1, ' ', 1)
print(2, ' ', 1, ' ', 2, ' ', 4, ' ', 8)
print(3, ' ', 1, ' ', 3, ' ', 9, ' ', 27)
print(4, ' ', 1, ' ', 4, ' ', 16, ' ', 64)
print(5, ' ', 1, ' ', 5, ' ', 25, ' ', 125)
