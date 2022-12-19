import random
i = 1
n = int(random.randrange(2,2**200))


while n > 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
    print("Step: " + str(i) + " , Digit = " + str(n))
    i+=1
