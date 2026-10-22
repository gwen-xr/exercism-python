def square(number):
    if number>64 or number <1:
        raise ValueError("square must be between 1 and 64")
    num = int(number)
    grain = 2**(num-1)
    return grain    


def total():
    total_grain = 0
    for n in range(1,65):
        total_grain += square(n)
    return total_grain


