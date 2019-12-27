def high_and_low(numbers):
    ls = numbers.split(" ")
    ls = [int(i) for i in ls ]
    return str(max(ls)) + " " +  str(min(ls))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))  # return "542 -214"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"