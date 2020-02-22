'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    a=a+1
    print(a)


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    a = a+1
    return a # hint this is incomplete 


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a,b):
    #addition=a+b
    #addition
    return a + b


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    c= sum(a,b)
    d=inc_return(c)
    print(d)
    return d


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    return


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    # hint: you can add strings together 
    # in order to concatenate them
    return

y= sum_inc(5,4)
print(y)
inc(4)

def main():
    user_input=input('enter a number ')
    user_input2=input('enter a number ')
    sum_inc(int(user_input),int(user_input2))

if __name__== '__main__':
    main()    