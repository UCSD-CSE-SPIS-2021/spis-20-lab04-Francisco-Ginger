#Lab 04 Partners: Francisco Garcia; Ginger Smith
# warmup on recursion
# multiply without the '*' operator
#should work with positive and negative values of 
#a and b
def recproduct(a, b):
    #code goes here
    #basecase:
    if b == 0:
        return 0
    elif b > 0:
        return a + recproduct(a, b-1)

print(recproduct(-5,5))


