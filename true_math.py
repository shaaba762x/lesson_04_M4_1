from math import inf

def divide(first, second):
    if second==0:
        result_ = inf
        return result_
    result_ = first / second
    return result_

print(divide(1,0))