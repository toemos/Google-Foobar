'''
Repeated pattern emerges in sequential XOR.
n % 4 = 0, xor of range = n;
n % 4 = 1, xor of range = 1;
n % 4 = 2, xor of range = n+1;
n % 4 = 3, xor of range = 0;
'''
# ans = 0
# for x in range(100):
# 	ans = ans^x
# 	print("{} = {}".format(x, ans))
#
# 0 = 0
# 1 = 1
# 2 = 3
# 3 = 0
# 4 = 4
# 5 = 1
# 6 = 7
# 7 = 0
# 8 = 8
# 9 = 1
# 10 = 11

'''
To calculate XOR of a range not starting at 0, take XOR 0-n of the number preceding our range, and XOR 0-n of the
last number in our range. Resulting XOR of these two calculations is equal to the XOR of our full range.
i.e. for range n-m:
XOR of single bit - 0-n | XOR of single bit n-m | Resulting XOR
0 (even 1's)            | 0 (even 1's)          | 0
0 (even 1's)            | 1 (odd 1's)           | 1
1 (odd 1's)             | 0 (odd 1's)           | 1
1 (odd 1's)             | 1 (even 1's)          | 0
'''


def solution(start, length):
    checksum = 0
    xorarray = []
    for x in range(length):
        linestartxor = xorrangefrom0(start + x * length - 1)
        lineendxor = xorrangefrom0(start + x * length + length - 1 - x)
        xorarray.append(linestartxor ^ lineendxor)
    for i in xorarray:
        checksum = checksum ^ i
    return checksum


def xorrangefrom0(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    if n % 4 == 3:
        return 0
