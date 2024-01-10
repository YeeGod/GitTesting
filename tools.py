

def Sum(a, b) :
    ans = 0
    for i in range(a, b+1) :
        ans += i
    return ans        

def productSum(a, b) :
    ans = 1
    for i in range(a, b+1) :
        ans *= i
    return ans