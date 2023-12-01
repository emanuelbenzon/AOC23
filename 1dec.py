with open("in.txt") as f:
    input = f.read()

svar1 = 0
for line in input.split("\n"):
    first = None
    last = None
    for i in line:
        if i.isdigit():
            last = i
            if first is None:
                first = i
    svar1 += int(first + last)

print(svar1)





dict = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        }

svar2 = 0
for line in input.split("\n"):
    first = None
    last = None
    string = ""
    for i in line:
        num = None
        if i.isdigit():
            num = i
        else:
            string += i
            for key,val in dict.items():
                if string.endswith(key):
                    num = str(val)
        if num != None:
            last = num
            if first is None:
                first = num

    svar2 += int(first + last)
    

print(svar2)