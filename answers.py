# Mahathir Rojan 

# ----------Question 1 -------------- 
def isIncreasing(L):
    """Write a function named *isIncreasing* that takes a list of integers as
    a parameter. *isIncraasing* should return *True* if it continually
    increases. That is given a parameter list L, then L[0] < L[1] < L[2]
    etc. otherwise return *False*."""
    count = 0
    for i in range(len(L)-2): 
        if L[i] < L[i+1] < L[i+2]:
            i = i + 1
            x = True 
        else: 
            x = False
    return x 
        

catalog = [1, 2, 3, 4,5,6,7,8,9,10,12,14]
catlog = [1,2,1,3]

# ----------Question 2----------------
def NumConvert(number):
    """Write a function named *NumConvert*. It should take a list of single
    digit numbers and convert it to an integer and return it.

    For example NumConvert([3,5,1]) would return the number 351.

    Assume all items in the list are positive single digits."""
    empty = "" 
    for i in number: 
        x = str(i) 
        y = "".join(x)
        empty = empty + y 
        z = int(empty)
    return z

# -----------Question 3----------------
def BinConvert(binary):
    """Write a function named *BinConvert* that takes a string representing a
    binary number and returns an integer with that number converted to
    decimal."""
    index = binary[::-1]
    total = 0 
    count = 1 
    uno = str(1)
    for x in index:
        if x == uno:
            total = total + count
        count = count * 2
    return total 

def tests():
    print ("--------Question 1-----------")
    print(isIncreasing(catalog))
    print(isIncreasing(catlog))
    print("-----------Question 2--------")
    print(NumConvert([3,5,1]))
    print(NumConvert([1,2,3,4,5,6,7,8,9]))
    print("---------Question 3-------")
    print(BinConvert("1"))
    print(BinConvert("10"))
    print(BinConvert("11"))
    print(BinConvert("100"))
    print(BinConvert("101"))
    print(BinConvert("1011"))
if __name__ == "__main__":
    tests()