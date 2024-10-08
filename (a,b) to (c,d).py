# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:26:49 2024

@author: morin
"""
from collections import deque
def isPossible(a, b, c, d):
    if a > 1000 or b > 1000 or c > 1000 or d > 1000:
        return "No"
    pairs = deque()
    pairs.append((a, b))
    print(pairs)
    counter = 0
    while pairs:
        key, value = pairs.popleft()
        print(pairs)
        print(key)
        print(value)
        if key == c and value == d:
            return "Yes"
        _sum = key + value
        print("counter", counter, _sum)
        if _sum <= c:
            pairs.append((_sum, value))
            print("pairs after test on c", pairs)
        if _sum <= d:
            pairs.append((key, _sum))
            print("pairs after test on d", pairs)
        counter =+ 1

    return "No"

# Example usage
a = 1
b = 1
c = 5
d = 2
result = isPossible(a, b, c, d)
print(result)