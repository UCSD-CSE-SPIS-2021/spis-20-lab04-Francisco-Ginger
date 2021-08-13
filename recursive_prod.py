def rec_product(a, b):

    '''Calculate product a * b recursively'''
     #code goes here
    if b == 0:
        return 0
    elif b < 0:
        return -a + rec_product(a,b+1)
    elif b > 0:
        return a + rec_product(a, b-1)

print(rec_product(0,5))
print(rec_product(1,5))
print(rec_product(-1,5))
print(rec_product(5,-2))
print(rec_product(-2,-2))
print(rec_product(5,-1))
print(rec_product(-5,-1))