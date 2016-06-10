def square(x):
    return x*x
def cube(x):
    return square(x)*x
def sum_from_a_to_b(a,b,function):
    currentSum = 0
    for x in range(a,b+1):
        currentSum = currentSum + function(x)
    return currentSum
 #now lets use it
print( sum_from_a_to_b(1,10,square) ) # will print the sum of the squares
print( sum_from_a_to_b(1,10,cube) ) 