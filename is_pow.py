import math
# Given an integer n, return true if it is a power of ten. Otherwise, return false.
# An integer n is a power of ten, if there exists an integer x such that n == 10^x

def is_natural_number(x):
    if x == 0:
        return True
    elif int(x) == 0:
        return False
    return x/int(x) == 1


def is_pow_of_base(number, base, precision=5):
    if number <= 0:
        return False
    result = round(math.log(number, base),5)
    return is_natural_number(result)

def is_power_of_ten(number):
    return is_pow_of_base(number, 10)

if __name__ == "__main__":
    print(is_power_of_ten(1))  # true
    print(is_power_of_ten(10))  # true
    print(is_power_of_ten(1000))  # true
    print(is_power_of_ten(5))  # false
    print(is_power_of_ten(20))  # false
    print(is_power_of_ten(-1))  # false
    print(is_power_of_ten(0.00001))  # true
