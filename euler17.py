belowTwenties = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
thousand = "thousand"


def getLength(n):
    text = ""
    while(n > 0):
        if n == 1000:
            text = "Onethousand"
            break
        elif n >= 100:
            rest = n % 100
            text += belowTwenties[(n - rest) / 100] + \
                hundred + ("and" if rest > 0 else "")
            n = rest
        elif n >= 20:
            rest = n % 10
            text += tens[(n - rest) / 10 - 2]
            n = rest
        elif n > 0:
            text += belowTwenties[n]
            n = 0

    return len(text)

print((sum([getLength(x) for x in range(1, 1001)])))
