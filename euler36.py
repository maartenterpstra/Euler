# test if a string is equal to its reverse
def palindromic(n):
    return n == n[::-1]

print(sum([x for x in range(1, 1000000) if palindromic(
    str(x)) and palindromic(bin(x)[2:])]))
