def rec_product(a, b):

    '''Calculate product a * b recursively'''
     #code goes here
    if b == 0:
        return 0
    # Code for when b is negative
    elif b < 0:
        return -a + rec_product(a,b+1)
    # Code for when b is positive
    elif b > 0:
        return a + rec_product(a, b-1)

print(rec_product(0,5))
print(rec_product(1,5))
print(rec_product(-1,5))
print(rec_product(5,-2))
print(rec_product(-2,-2))
print(rec_product(5,-1))
print(rec_product(-5,-1))