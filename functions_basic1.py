#1
def a():
# Function a
    return 5
    # a() will now be replaced with 5
print(a())
# Function a was called, so this will print out 5


#2
def a():
# Waiting for function a to be called
    return 5
    # function a() will be replaced with 5
print(a()+a())
# Function a() was called, this will now print the answer to 5+5.
# Will print out 10.


#3
def a():
# waiting for function a() to be called
    return 5
    # function a() will be replaced with 5
    return 10
    # this will be ignored bc it was previously already returned
print(a())
# will print out 5


#4
def a():
# waiting for a() to be called
    return 5
    # a() will be replaced with 5
    print(10)
    # this will be ignored bc we immediately left the function after 5 was returned
print(a())
# will print out 5


#5
def a():
# waiting on a() to be called
    print(5)
    # will print out 5, once function is called
x = a()
# function a() is now called
# printed 5
print(x)
# there is no value to x, so x = nothing


#6
def a(b,c):
# waiting on a(b,c) to be called
    print(b+c)
    # first a funcation 1+2=3, will print out 3
    # second a funcation 2+3=5, will print out 5
print(a(1,2)+a(2,3))
# will print out 8




#7
def a(b,c):
# function
    return str(b)+str(c)
    # b=2 c=5
    # will not be returned mathematically, but will be returned as a string 2+5=25
print(a(2,5))
# will print out 25



#8
def a():
    b = 100
    print(b)
    # will print out 100
    if b < 10:
    # 100 is not less than 5, so will not return 5
        return 5
    else:
    # 10 will be in place of the a function
        return 10
    return 7
    # 7 will be ignored bc we are already out of the function
print(a())
# will print out 100, 10


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
# b=2 c=3
# 2 is less than 3, so will return & print as 7
print(a(5,3))
# b=5 c=3
# 5 is not less than 3, so will return & print 14
print(a(2,3) + a(5,3))
# first a function b=2 c=3, is returned as 7
# second a funcation b=5 c=3, is returned as 14
# 7+14=21
# will be printed as 7, 14, 21


#10
def a(b,c):
    return b+c
    # b=3 c=5, 3+5=8, 8 is returned
    return 10
    # this return is ignored, as we've already left out of the function
print(a(3,5))
# will print as 8


#11
b = 500
print(b)
# first will print 500
def a():
    b = 300
    print(b)
print(b)
# second will print as 500
a()
# function was called
# inside function b=300
# third will print as 300
print(b)
# fourth will print out 500
# 300 was only inside function, which is why we don't print out 300
# will print as 500, 500, 300, 500


#12
b = 500
print(b)
# first will print as 500
def a():
    b = 300
    print(b)
    return b
print(b)
# second will print as 500
a()
# function was called, b=300
# third will print as 300
# 300 will be returned to a(), but does not request to print it, so it didn't really do anything
print(b)
# fourth will print as 500
# will print as 500, 500, 300, 500


#13
b = 500
print(b)
# first will print as 500
def a():
    b = 300
    print(b)
    return b
print(b)
# second will print as 500
b=a()
# a function was called
# third will print as 300
# b=300 now, after 300 was returned
print(b)
# fourth will print as 300
# will print as 500, 500, 300, 300


#14
def a():
    print(1)
    # 2) will print 1
    b()
    # 3) b function is now called, so move to function b
    print(2)
    # 5) will print 2
def b():
    print(3)
    # 4) will print 3, go back to finish off function a
a()
# 1) a function is called
# will print as 1, 3, 2


#15
def a():
    print(1)
    # 2) will print 1
    x = b()
    # 3) function b() is called
    # 6) x=5
    print(x)
    # 7) will print 5
    return 10
    # 8) will return 10 to y
def b():
    print(3)
    # 4) will print 3
    return 5
    # 5) finish off this function by returning 5 to x
y = a()
# 1) function a() is called
# 9) y=10
print(y)
# 10) will print 10
# will print 1, 3, 5, 10
