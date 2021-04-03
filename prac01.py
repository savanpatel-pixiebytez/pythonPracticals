def isPrime(val):
    for i in range(1, int(val/2)):
        if val % i == 0:
            return False
    return True


def isArmstrong(val):
    tmp = val
    sum = 0
    while(tmp != 0):
        rem = tmp % 10
        sum = sum + (rem ** len(str(val)))
        tmp = tmp // 10
    return sum == val


def fibonacciSeq(val):
    if val < 0:
        print("Incorrect input")

    elif val == 0:
        print(0)
        return 0

    elif val == 1 or val == 2:
        print(1)
        return 1
    else:
        arr = []
        arr.append(0)
        arr.append(1)
        for i in range(2, val):
            arr.append(arr[i-1] + arr[i-2])

        return arr


def swap(a, b):

    if type(a) == int and type(b) == int:
        a, b = b, a
    return a, b


def factFor(val):
    tmp = 1
    if val == 0:
        return tmp
    else:
        for i in range(1, val+1):
            tmp = tmp * i
        return tmp


def factRecursion(val):
    if val == 0:
        return 1
    else:
        return val * factRecursion(val-1)


print("Is prime number => ", isPrime(10))
print("Armstrong => ", isArmstrong(154))
print("This is fibonacci series => ", fibonacciSeq(10))
print("Swap => ", swap(10, 5))
print("Factorial with for loop => ", factFor(10))
print("Factorial with recursion => ", factRecursion(10))
